from django.db import models

# Create your models here.
from district.models import District


class Institute(models.Model):
    ins_id = models.IntegerField(primary_key=True)
    ins_name = models.CharField(max_length=200, unique=True)
    dist_id = models.ForeignKey(District)