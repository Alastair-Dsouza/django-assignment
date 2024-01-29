from django.db import models

# Create your models here.
class User(models.Model):

    def __str__(self):
        return self.user_name

    user_email = models.CharField(max_length = 200,unique = True)
    user_name = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)
    
