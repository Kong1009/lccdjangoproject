from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    imglink = models.CharField(max_length=255)
    date = models.DateField()

    
    class Meta:
        db_table = "news"
