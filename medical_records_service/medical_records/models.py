from django.db import models

class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icd_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatment_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    drug_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient_id = models.IntegerField()
    record_date = models.DateField()
    doctor_id = models.IntegerField()
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f"Medical Record {self.id} for patient {self.patient_id}"

class Prescription(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"Prescription {self.id} for medical record {self.medical_record_id}"
