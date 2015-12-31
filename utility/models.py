import os,uuid
from datetime import datetime


from django.db import models


# Create your models here.

def user_data_file_path(instance, filename):
    name, ext = os.path.splitext(filename)
    file_path = os.path.join('csv', str(uuid.uuid4().fields[-1])[:4], datetime.now().strftime("%Y/%m"), filename)
    return file_path

class FileUpload(models.Model):
    interval = models.ForeignKey('basehandler.IntervalData')
    data_file = models.FileField(upload_to=user_data_file_path)
    status = models.CharField(default='To be Upload', max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.data_file.name

    class Meta:
        verbose_name = 'Upload data file'
        verbose_name_plural = 'Upload data files'
