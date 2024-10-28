from django.db import models
from django.contrib import admin
class ClientInfo(models.Model):
    full_name = models.CharField(max_length=120)
    account_id = models.InterField(primary_key="account_id")
    Phone_Number = models.InterField()
    Loan_amount = models.InterField()
    Time_period = models.FloatField()
    Interest = models.FloatField()


class Clientinfoadmin(admin,ModelAdmin):
    list_display=('full_name','account-id','Phone_Number','Loan_amount','Time_period','Interest')