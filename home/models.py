from django.db import models

# Create your models here.
def get_upload_path(instance,filename):
    return 'certificates/{0}/{1}'.format(instance.roll_no,filename)
class Student(models.Model):
    roll_no = models.CharField(primary_key=True,max_length=12)
    certificate = models.ImageField(upload_to=get_upload_path,max_length=None)

    def __str__(self):
        return self.roll_no