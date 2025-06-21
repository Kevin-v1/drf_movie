from rest_framework import serializers
from .models import Card, Order

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'card_name', 'card_price', 'duration', 'info']

class OrderSerializer(serializers.ModelSerializer):
    card = CardSerializer()
    
    class Meta:
        model = Order
        fields = '__all__'