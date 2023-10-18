from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# Create your models here.
