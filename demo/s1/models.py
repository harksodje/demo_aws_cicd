from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table: 'User'
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
