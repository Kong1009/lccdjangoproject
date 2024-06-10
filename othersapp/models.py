from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    

    
    class Meta:
        db_table = "contact"
