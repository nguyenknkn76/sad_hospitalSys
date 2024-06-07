from rest_framework import serializers
from .models import Doctor, DoctorLicense, Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        specialty_data = validated_data.pop('specialty')
        specialty = Specialty.objects.create(**specialty_data)
        doctor = Doctor.objects.create(specialty=specialty, **validated_data)
        return doctor

    def update(self, instance, validated_data):
        specialty_data = validated_data.pop('specialty')
        
        Specialty.objects.filter(id=instance.specialty.id).update(**specialty_data)
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance

class DoctorLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorLicense
        fields = '__all__'

