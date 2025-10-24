from django.contrib import admin
from portal.models import Students

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'dob', 'marks', 'email', 'phone_number', 'address']

admin.site.register(Students, StudentsAdmin)