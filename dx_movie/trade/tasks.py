from datetime import timedelta

from django.utils import timezone
from celery import shared_task

from .models import Order

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def check_order_expired(order_id):
    order = Order.objects.get(id= order_id)
    expired_time = order.pay_time + timedelta(minutes=30)
    if timezone.now() > expired_time:
        order.pay_status = 'TRADE_CLOSED'
        order.save()
        return f'order {order.id} 过期，订单状态close'
    else:
        return f'order {order.id} 未过期，订单状态paying'

@shared_task
def batch_check_expired_orders():
    orders = Order.objects.filter(pay_status='PAYING')
    for order in orders:
        check_order_expired.delay(order.id)
    
