from django.db import models

class paymentModel(models.Model):
    active      = models.BooleanField(default=True)
    name        = models.CharField(max_length=30)
    email       = models.EmailField()
    message     = models.TextField()
    time        = models.DateField(auto_now_add=True)