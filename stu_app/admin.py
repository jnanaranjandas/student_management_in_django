from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username','user_type','email','profile_pic']

admin.site.register(CustomUser,UserModel)


admin.site.register(Course)
admin.site.register(SessionYear)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(StaffNotification)
admin.site.register(StaffLeave)
admin.site.register(StaffFeedback)
admin.site.register(StudentNotification)
admin.site.register(StudentFeedback)
admin.site.register(StudentLeave)
admin.site.register(Attendance)
admin.site.register(Attendance_report)
admin.site.register(StudentResult)










