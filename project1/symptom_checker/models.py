from django.db import models
class web1(models.Model):
    news_head=models.CharField(max_length=225)
    news_web=models.CharField(max_length=225)
    Date=models.DateField()

# Create your models here.
