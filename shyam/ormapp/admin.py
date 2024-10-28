from django.contrib import admin 
from .models import ClientInfo,ClientInfoAdmin
admin.site.register(ClientInfo,ClientInfoAdmin)