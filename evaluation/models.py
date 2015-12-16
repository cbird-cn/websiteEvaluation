from django.db import models
from django.contrib import admin
# Create your models here.

class case(models.Model):
	caseName=models.CharField(max_length=50)
	#fenlei
	catogaryName=models.CharField(max_length=50)
	catogaryDetailName=models.CharField(max_length=50)
	attribute=models.CharField(max_length=50)
	evaluation=models.CharField(max_length=50)
'''
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')
'''
admin.site.register(case)