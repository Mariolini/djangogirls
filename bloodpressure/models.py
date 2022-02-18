from django.db import models
from django.conf import settings
from django.utils import timezone

class BpEntry(models.Model):
    messure_date = models.DateTimeField(default=timezone.now)
    systolic = models.PositiveSmallIntegerField(default=130)
    diastolic = models.PositiveSmallIntegerField(default=90)
    pulse = models.PositiveSmallIntegerField(default=80)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Zeit: {self.messure_date} systolisch: {self.systolic} diastolisch: {self.diastolic}"

# Create your models here.
