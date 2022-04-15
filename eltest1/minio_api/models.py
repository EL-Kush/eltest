from django.db import models

# Create your models here.
def file_name(instance, filename):
    name = filename.split('.')[-1]
    filename = '{}.{}'.format('ELTEST', name)
    return filename

class FileUpload(models.Model):
    file = models.FileField(upload_to=file_name)