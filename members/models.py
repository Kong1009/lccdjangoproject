from django.db import models


class Members(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    
    class Meta:
        db_table = "members"
