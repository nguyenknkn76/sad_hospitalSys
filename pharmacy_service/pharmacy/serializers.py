from rest_framework import serializers
from .models import Inventory, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), source='supplier')

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'quantity', 'unit', 'supplier_id', 'expiry_date']
