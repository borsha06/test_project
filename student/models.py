from django.db import models

# Create your models here.
from district.models import District
from institute.models import Institute


class Student(models.Model):
    std_id = models.IntegerField(primary_key=True)
    std_name = models.CharField(max_length=200)
    dist_id = models.ForeignKey(District)
    ins_id = models.ForeignKey(Institute)
    std_phone = models.CharField(max_length=15, unique=True)
    std_admission = models.DateField()

