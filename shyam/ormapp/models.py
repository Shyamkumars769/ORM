from django.db import models
from django.contrib import admin
class ClientInfo(models.Model):
    full_name = models.CharField(max_length=120)
     = models.IntegerField(primary_key="account_id")
    IFSC_code = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Loan_amount = models.IntegerField()
    Interest = models.FloatField()
    


class ClientInfoAdmin(admin.ModelAdmin):
    list_display=('full_name','account_no','IFSC_code','branch','Phone_Number','Loan_amount','Interest')