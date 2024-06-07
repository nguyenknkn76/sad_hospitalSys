from django.db import models

class Appointment(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Canceled', 'Canceled')])

    def __str__(self):
        return f"Appointment {self.id} - {self.patient_id} with {self.doctor_id} on {self.appointment_date} at {self.appointment_time}"
