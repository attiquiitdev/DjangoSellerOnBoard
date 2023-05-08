from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=200)
    balance = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    NETWORK_CHOICES = [
        ('Polygon', 'Polygon'),
        ('Ethereum', 'Ethereum')
    ]
    network = models.CharField(max_length=200, choices=NETWORK_CHOICES)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)