from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICE =[
        (MEMBERSHIP_BRONZE,'BRONZE'),
        (MEMBERSHIP_SILVER,'SILVER'),
        (MEMBERSHIP_GOLD,'GOLD')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.Charfield(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)

class Oder(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING,'PENDING'),
        (PAYMENT_COMPLETE,'COMPLETE'),
        (PAYMENT_FAILED,'FAILED')
    ]
    placed_at = models.DateTimeField(auto_now_add= True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) # connection to one to one relation and its child thats why define here
                                                                                            # in child define the parent
