from django.db import models

from basehandler.models import Company, Parameter, IntervalData
# Create your models here.


class CompanyStatsFigure(models.Model):
    company = models.ForeignKey(Company)
    param = models.ForeignKey(Parameter)
    interval = models.ForeignKey(IntervalData)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    @classmethod
    def bulk_create_data(cls, data):
        cls.objects.bulk_create(data)
