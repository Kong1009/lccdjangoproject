from django.db import models

# Create your models here.
class Members(models.Model):
    username = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)

    class Meta:
        db_table = "members"