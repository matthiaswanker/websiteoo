from django.contrib import admin
from .models import  Client,Advisor,Bank,Investment,Stock

# # Register your models here.
admin.site.register(Client)
admin.site.register(Advisor)
admin.site.register(Bank)
admin.site.register(Investment)
admin.site.register(Stock)