from rest_framework import serializers
from .models import MedicalRecord, Diagnosis, Treatment, Medication, Prescription

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    diagnosis_id = serializers.PrimaryKeyRelatedField(queryset=Diagnosis.objects.all(), source='diagnosis')
    treatment_id = serializers.PrimaryKeyRelatedField(queryset=Treatment.objects.all(), source='treatment')

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient_id', 'record_date', 'doctor_id', 'diagnosis_id', 'treatment_id', 'notes']

    def create(self, validated_data):
        diagnosis = validated_data.pop('diagnosis')
        treatment = validated_data.pop('treatment')
        medical_record = MedicalRecord.objects.create(diagnosis=diagnosis, treatment=treatment, **validated_data)
        return medical_record

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
