from django.contrib import admin
from .models import Member,Enquiry,Plan, Attendance
# Register your models here.
admin.site.register(Member)
admin.site.register(Enquiry)
admin.site.register(Plan)
admin.site.register(Attendance)
