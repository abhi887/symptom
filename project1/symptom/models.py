from django.db import models

class log(models.Model):
    log_email=models.CharField(max_length=225)
    log_password=models.CharField(max_length=225)
class registeration(models.Model):
    reg_first=models.CharField(max_length=225)
    reg_last=models.CharField(max_length=225)
    reg_username=models.CharField(max_length=225)
    reg_email=models.CharField(max_length=225)
    reg_password=models.CharField(max_length=225)
    reg_confirm_password=models.CharField(max_length=225)
class contact(models.Model):
    contact_first=models.CharField(max_length=225)
    contact_last=models.CharField(max_length=225)
    contact_email=models.CharField(max_length=225)
    contact_subject=models.CharField(max_length=225)
    contact_feedback=models.CharField(max_length=225)
class diagnose(models.Model):
    diagnose_age=models.IntegerField()
    role=(
        ('male',"Male"),
        ('female',"Female")
    )
    diagnose_gender=models.CharField(max_length=10,choices=role,default='male')




# Create your models here.
