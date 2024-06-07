from rest_framework import serializers
from .models import Bill, Payment

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    bill_id = serializers.PrimaryKeyRelatedField(queryset=Bill.objects.all(), source='bill')

    class Meta:
        model = Payment
        fields = ['id', 'bill_id', 'payment_date', 'amount', 'payment_method', 'created_at']
