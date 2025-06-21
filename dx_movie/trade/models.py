from django.db import models

# Create your models here.
from django.db import models
from account.models import Profile

class Card(models.Model):
    card_name = models.CharField("会员卡名称",max_length=100, unique=True)
    card_price = models.DecimalField("价格", max_digits=8, decimal_places=2)
    duration = models.IntegerField("有效天数")
    info = models.CharField("会员卡简介",max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'card'
        verbose_name = "会员卡信息"
        verbose_name_plural = verbose_name


# Create your models here.
class Order(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("PAYING", "待支付"),
    )

    PAY_TYPE = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )

    user = models.ForeignKey(Profile, related_name='orders', to_field='uid',on_delete=models.CASCADE, verbose_name="用户")
    # 禁止反向
    card = models.ForeignKey(Card, related_name='+', on_delete=models.DO_NOTHING, verbose_name='会员卡')
    #订单号唯一
    order_sn = models.CharField("订单编号",max_length=30, null=True, blank=True, unique=True)
    # 支付宝交易号
    trade_no = models.CharField("交易号",max_length=100, unique=True, null=True, blank=True)
    #支付状态
    pay_status = models.CharField("订单状态",choices=ORDER_STATUS, default="PAYING", max_length=30)
    # 订单的支付类型
    pay_type = models.CharField("支付类型",choices=PAY_TYPE, default="alipay", max_length=10)
    order_mount = models.DecimalField("订单金额", max_digits=10, decimal_places=2)
    pay_time = models.DateTimeField("支付时间",null=True, blank=True)
    # 更新时间
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'order'
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)

