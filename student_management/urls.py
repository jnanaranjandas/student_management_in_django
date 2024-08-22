"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from stu_app import views,hod_views,staff_views,student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('',views.user_login,name='login'),
    path('dologin/',views.doLogin,name='dologin'),
    path('dologout/',views.doLogout,name='dologout'),

    # profile 
    path('profile/',views.profile,name="profile"),

    # update profile
    path('profile/update',views.ProfileUpdate,name='profile_update'),

    # # hod url
    path('hod/',hod_views.Hod_home,name='home'),
    path('hod/add_stu/',hod_views.AddStudent,name='add_stu'),
    path('hod/view_stu/',hod_views.ViewStudent,name='view_stu'),
    path('hod/stu_edit/<str:id>',hod_views.EditStudent,name='edit_stu'),
    path('hod/update_stu/',hod_views.UpdateStudent,name='update_stu'),
    path('hod/delete_stu/<str:admin>',hod_views.DeleteStudent,name='delete_stu'),

    # course
    path('hod/add_course/',hod_views.AddCourse,name='add_course'),
    path('hod/view_course/',hod_views.ViewCourse,name='view_course'),
    path('hod/edit_course/<str:id>',hod_views.EditCourse,name='edit_course'),
    path('hod/update_course',hod_views.UpdateCourse,name='update_course'),
    path('hod/course_delete<str:id>',hod_views.DeleteCourse,name='delete_course'),


    # staff
    path('hod/add_staff',hod_views.AddStaff,name='add_staff'),
    path('hod/view_staff',hod_views.ViewStaff,name='view_staff'),
    path('hod/edit_staff/<str:id>',hod_views.EditStaff,name='edit_staff'),
    path('hod/update_staff',hod_views.UpdateStaff,name='update_staff'),
    path('hod/staff_delete<str:admin>',hod_views.DeleteStaff,name='delete_staff'),

    path('hod/add_sub',hod_views.AddSubject,name='add_sub'),
    path('hod/view_sub',hod_views.ViewSubject,name='view_sub'),
    path('hod/edit_sub/<str:id>',hod_views.EditSubject,name='edit_sub'),
    path('hod/update_sub',hod_views.UpdateSubject,name='update_sub'),
    path('hod/sub_delete/<str:id>',hod_views.DeleteSubject,name='delete_sub'),


    path('hod/add_session',hod_views.AddSession,name='add_session'),
    path('hod/view_session',hod_views.ViewSession,name='view_session'),
    path('hod/edit_session<str:id>',hod_views.EditSession,name='edit_session'),
    path('hod/update_session',hod_views.UpdateSession,name='update_session'),
    path('hod/delete_session/<str:id>',hod_views.DeleteSession,name='delete_session'),
    path('hod/staff_send_notification',hod_views.Staff_Notification,name='staff_notification'),
    path('staff/save_notification',hod_views.SaveStaffNotification,name='save_notification'),

    path('hod/staff_leave_view',hod_views.StaffLeaveView,name='staff_leave_view'),
    path('hod/staff_approved_leave/<str:id>',hod_views.StaffApprovedLeave,name='staff_approved_leave'),
    path('hod/staff_disapproved_leave/<str:id>',hod_views.StaffDisApprovedLeave,name='staff_disapproved_leave'),
    path('hod/hod_staff_feedback',hod_views.HodStaffFeedback,name='hod_staff_feedback'),

    path('hod/hod_feedback_save',hod_views.HodFeedbackSave,name='hod_feedback_save'),

    path('hod/student_feedback_hod',hod_views.StudentFeedbackHod,name='stu_fedback_hod'),

    # staff urls
    path('staff/home',staff_views.Home,name='staff_home'),
    path('staff/notifications',staff_views.Notification,name='notification'),
    path('staff/mark_as_done/<str:status>',staff_views.Staff_Mark_Notification,name='staff_mark_as_done'),
    path('staff/apply_leave',staff_views.ApplyLeave,name='apply_leave'),
    path('staff/apply_leave_save',staff_views.ApplyLeaveSave,name='apply_leave_save'),

    path('staff/send_feedback',staff_views.Staff_Feedback,name='send_feedback'),
    path('staff/feedback_save',staff_views.Staff_Feedback_Save,name='save_feedback'),


    # student
    path('student/home',student_views.StudentHome,name='student_home'),
    path('hod/student_notification',hod_views.Student_Notification,name='student_notification'),
    path('hod/student_noti_save',hod_views.Student_Notification_Save,name='save_stu_noti'),

    path('student/stu_noti',student_views.Stu_Notification,name='stu_noti'),
    path('student/mark_as_done/<str:status>',student_views.Student_Mark_as_done,name='stu_mark_as_done'),
    path('student/stu_feedback',student_views.Student_Feedback,name='stu_feedback'),
    path('student/feedback_save',student_views.StuFeedbackSave,name='stu_fed_save'),



    path('hod/reply_stu_feed',hod_views.StudentFeedbackReply,name='reply_stu_feed'),

    path('student/apply_stu_leave',student_views.Student_Leave,name='apply_stu_leave'),
    path('student/leave_stu_save',student_views.StudentLeaveSave,name='leave_stu_save'),


    path('hod/student_leave_view',hod_views.StudentLeaveView,name='stu_leave_view'),

    path('hod/student_approved_leave/<str:id>',hod_views.StudentApprovedLeave,name='stu_approved_leave'),

    path('hod/student_disapproved_leave/<str:id>',hod_views.StudentDisApprovedLeave,name='stu_disapproved_leave'),


    path('staff/take_attendance',staff_views.StaffTakeAttendance,name='staff_take_attendance'),

    path('staff/save_attendance',staff_views.StaffSaveAttendance,name='staff_save_attendance'),
    
    path('staff/view_attendance',staff_views.ViewAttendance,name='staff_view_attendance'),

    path('staff/stu_view_attendance',student_views.Student_view_Attendance,name='stu_view_attendance'),

    path('hod/view_stu_attendance',hod_views.ViewStuAttendance,name='stu_view_attten'),


    path('staff/add_result',staff_views.StaffAddResult,name='staff_add_result'),
    
    path('staff/save_result',staff_views.StaffSaveResult,name='staff_save_result'),

    path('student/view_result',student_views.ViewResult,name='view_result')

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





