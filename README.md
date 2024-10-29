# Ex02 Django ORM Web Application
## Date:29-10-2024 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Client paint.png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```

models.py 

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


admin.py


from django.contrib import admin 
from .models import ClientInfo,ClientInfoAdmin
admin.site.register(ClientInfo,ClientInfoAdmin)



```


## OUTPUT

Include the screenshot of your admin page.

![alt text](<Screenshot 2024-10-29 003745.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
