from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
