from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


    def __str__(self) -> str:
        return str(self.name)

class House(models.Model):
    number = models.IntegerField()
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    rent = models.IntegerField()

    def __str__(self) -> str:
        return str(self.number)

class RentRecord(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField()
    confirmation_code = models.CharField(max_length=50)
