from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length = 30)
    semester = models.IntegerField()
    uRollNo = models.IntegerField(verbose_name='University Roll no:')
    