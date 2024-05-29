from django.contrib import admin
from .models import Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'number', 'gender', 'qualification', 'speciality', 'hospital', 'availability','percentage', 'start', 'end', 'profilepic')
    list_filter = ('id','number')
    search_fields = ('id','name', 'number')



admin.site.register(Doctor, DoctorAdmin)

