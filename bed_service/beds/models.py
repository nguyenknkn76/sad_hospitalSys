from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Bed(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Maintenance', 'Maintenance')])
    patient_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Bed {self.bed_number} in {self.clinic.name}"
