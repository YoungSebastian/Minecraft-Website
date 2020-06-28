from django.db import models
from django import forms

from captcha.fields import ReCaptchaField

topics = (
    ('payment', 'Płatność'),
    ('server', 'Usprawnienie servera.'),
    ('rofl', 'Admin daj moda.'),
    ('other', 'Inne.'))

class messageModel(models.Model):
    name    = models.CharField(max_length=30)
    email   = models.EmailField()
    topic   = models.CharField(max_length=30)
    message = models.TextField()

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()
