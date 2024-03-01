from django.db import models
import random

class Sale(models.Model):
    GENDER_CHOICES = [
        ('1', 'Male'),
        ('0', 'Female'),
    ]

    CATEGORY_CHOICES = [
        ('0', 'Clothing'),
        ('1', 'Electronics'),
        ('2', 'Food'),
        ('4', 'Books'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('1', 'Credit Card'),
        ('2', 'Debit Card'),
        ('3', 'Cash'),
        ('0', 'Online Payment'),
    ]

    gender = models.CharField(max_length=55, choices=GENDER_CHOICES)
    age = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    shopping_mall = models.CharField(max_length=100)

    def __str__(self):
        return f"Random Number - {self.shopping_mall}"


    def __str__(self):
        return f"Sale - {self.id}"

