from django.contrib import admin
from .models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name', 'description', 'created', 'updated']
	list_editable = ['first_name','last_name',]
	list_per_page = 10



admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
