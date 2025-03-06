from django.db import models
from django.utils.timezone import now


class Data(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class Students(models.Model):
    STATUS_CHOICES = [
        ('pending', '⏳ Kutmoqda'),
        ('present', '✔ Bor'),
        ('absent', '❌ Yo‘q'),
    ]

    fullname = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='students', null=True, blank=True)


    def __str__(self):
        return f'{self.fullname} - {self.status} - {self.data}'
