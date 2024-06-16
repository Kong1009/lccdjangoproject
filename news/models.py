from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    imglink = models.CharField(max_length=255)
    platform = models.CharField(max_length=50)
    classification = models.CharField(max_length=50, default='經濟')
    date = models.DateField()

    
    class Meta:
        db_table = "news"
