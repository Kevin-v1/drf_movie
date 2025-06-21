from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework import viewsets
from .models import Card, Order
from .serializers import CardSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.zhifubao import Alipay
from utils.errors import TradeError,response_data
from utils.common import get_random_code
from django.utils import timezone
from account.models import Profile
from django.conf import settings
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from utils.filters import OrderFilter
from .tasks import add,mul,xsum

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('-id')
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()] # 只有登录用户可以查看订单
        else:
            return [IsAdminUser()] # 只有管理员可以修改订单

class AlipayAPIView(APIView):
    def get(self, request):
        card_id = request.GET.get('card_id',None)
        print(card_id)
        try:
            card = Card.objects.get(pk=card_id)
        except:
            return Response(response_data(*TradeError.CardParamError))
        order_sn = request.GET.get('order_sn', None)
        if not order_sn:
            out_trade_no = "pay" + datetime.now().strftime("%Y%m%d%H%M%S") + get_random_code(4)
            # 创建订单
            try:
                Order.objects.create(
                    user = Profile.objects.get(user=request.user),
                    card = card,
                    order_sn=out_trade_no,
                    order_mount=card.card_price,
                    pay_time = timezone.now(),
                )
                print("创建订单时间：",timezone.now())
            except:
                return Response(response_data(*TradeError.OrderCreateError))
        else:
            try:
                order = Order.objects.get(order_sn=order_sn)
                if order.pay_status != 'PAYING':
                    return Response(response_data(*TradeError.OrderStatusError))
                out_trade_no = order_sn
            except:
                return Response(response_data(*TradeError.OrderStatusError))
        # 生成支付宝支付链接
        try:
            alipay = Alipay()
            pay_url = alipay.trade_page(
                out_trade_no=out_trade_no,
                total_amount=str(card.card_price),
                subject=card.card_name,
                body='支付宝支付',
                product_code="FAST_INSTANT_TRADE_PAY"
            )
            return Response(pay_url)
        except:
            return Response(response_data(*TradeError.AlipayRequestError))

class AlipayCallbackAPIView(APIView):
    def post(self, request):
        parms = request.POST.dict()
        print(parms)
        # 去除sign 和 sign_type
        sign = parms.pop('sign') # 删除sign
        del parms['sign_type'] # 删除sign_type
        # 对字典排序
        sorted_list = sorted((k,v) for k,v in parms.items()) #数据简短示例：[('app_id', '2021001176644228'), ... ,('version', '1.0')]
        unsign_string = '&'.join(f"{k}={v}" for k,v in sorted_list) #简短示例：app_id=2021001176644228&biz_content=%7B%22out_trade_no
        # 验证签名
        alipay = Alipay()
        if not alipay.verify_sign(unsign_string, sign):
            print('verify_sign error')
            return Response('error')
        
        print('verify_sign success')
        try:
            order_sn = parms.get('out_trade_no')
            order = Order.objects.get(order_sn=order_sn)
        except:
            return Response('error')
        # 验证金额
        if parms.get('total_amount') != str(order.order_mount):
            print('金额不一致')
            return Response('error')
        # 验证seller_id
        if parms.get('seller_id') != settings.ALIPAY_SELLER_ID:
            print('seller_id不一致')
            return Response('error')
        # 验证app_id
        if parms.get('app_id') != settings.ALIPAY_APP_ID:
            print('app_id不一致')
            return Response('error')
        # 验证交易状态
        if parms.get('trade_status') not in ['TRADE_SUCCESS', 'TRADE_FINISHED']:
            print('交易状态不一致')
            return Response('error')
        print('全部验证通过')
        # 更改order表
        with transaction.atomic():
            order.trade_no = parms.get('trade_no')
            order.pay_status = parms.get('trade_status')
            order.pay_time = timezone.now()
            order.save()
        # 更改profile表
            profile = Profile.objects.get(uid=order.user.uid)
            profile.is_upgrade = 1
            profile.upgrade_time = timezone.now()
            profile.upgrade_count += 1
            if not profile.expire_time or profile.expire_time < timezone.now():
                profile.expire_time = timezone.now() + timedelta(days=order.card.duration)
            else:
                profile.expire_time += timedelta(days=order.card.duration)
            profile.save()
        return Response('success')
    
class TaskAPIView(APIView):

    def get(self, request):
        result1 = add.delay(3,4)
        print(f'add:{result1}')

        result2 = mul.delay(4,5)
        print(f'mul:{result2}')

        result3 = xsum.delay([1,2,3])
        print(f'xsum:{result3}')
        
        return Response('执行task')