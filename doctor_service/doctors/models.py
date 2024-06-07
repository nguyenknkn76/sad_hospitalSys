from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DoctorLicense(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.license_number} ({self.license_type})"
