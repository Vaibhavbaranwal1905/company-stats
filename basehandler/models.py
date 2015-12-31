from django.db import models

# Create your models here.
class Company( models.Model ):
    """ Stores all the Company records. """

    name = models.CharField( max_length = 50 , unique=True)
    objects = models.Manager()

    def __unicode__( self ):
        return self.name

    class Meta:
        ordering = ['name']


class Parameter( models.Model ):
    """ Stores all the Parameter records. """

    name = models.CharField( max_length = 50 , unique=True)
    weightage = models.DecimalField(max_digits=5, decimal_places=2)
    objects = models.Manager()

    def __unicode__( self ):
        return self.name

    class Meta:
        ordering = ['name']

class IntervalData( models.Model ):
    """ Stores all the Parameter records. """

    name = models.CharField( max_length = 50 , unique=True)
    objects = models.Manager()

    def __unicode__( self ):
        return self.name

    class Meta:
        ordering = ['name']
