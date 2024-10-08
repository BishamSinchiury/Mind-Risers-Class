from django.db import models #type: ignore
from django.contrib.auth.models import AbstractUser #type: ignore

class User(AbstractUser):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    image = models.ImageField()
    phone_number = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS : list = []

class ProductType(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    department = models.ManyToManyField("Department") 
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity =models.FloatField(null=True)
    price = models.FloatField()
    vendor = models.ForeignKey("Vendor", on_delete=models.SET_NULL, null=True)

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)

class Vendor(models.Model):
    name  = models.CharField(max_length=300)
    phone_number = models.IntegerField()
    email =  models.EmailField(unique=True)

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)

class Customer(models.Model):
    name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField()
