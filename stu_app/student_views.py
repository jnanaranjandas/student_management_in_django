from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


def StudentHome(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_male = Student.objects.filter(gender='male').count()
    student_female = Student.objects.filter(gender='female').count()

    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_male' : student_male,
        'student_female' : student_female
    }

    return render(request,'Student/stu_home.html',context)


def Stu_Notification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = StudentNotification.objects.filter(student_id = student_id)

    return render(request,'Student/stu_notification.html',{'notification':notification})



def Student_Mark_as_done(request,status):
    notification = StudentNotification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('stu_noti')

def Student_Feedback(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = StudentFeedback.objects.filter(student_id = student_id)

    return render(request,'Student/stu_feedback.html',{'feedback_history':feedback_history})


def StuFeedbackSave(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)

        feed = StudentFeedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = ""
        )

        feed.save()
        return redirect('stu_feedback')

    

def Student_Leave(request):
    student = Student.objects.get(admin = request.user.id)
    student_leave_history = StudentLeave.objects.filter(student_id = student)

    return render(request,'Student/apply_leave.html',{'student_leave_history':student_leave_history})



def StudentLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin = request.user.id)
        student_leave = StudentLeave(student_id = student_id,data = leave_date,message = leave_message)
        student_leave.save()
        messages.success(request,'Leave Successfully Send')
        return redirect('apply_stu_leave')
    

    


def Student_view_Attendance(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)

    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

            # attendance = Attendance.objects.get(subject_id = get_subject)
            attendance_report = Attendance_report.objects.filter(student_id = student,attendance_id__subject_id = subject_id)



    return render(request,'Student/stu_view_attendance.html',{'subjects':subjects,'action':action,'get_subject':get_subject,'attendance_report':attendance_report})



def ViewResult(request):
    student = Student.objects.get(admin = request.user.id)
    result = StudentResult.objects.filter(student_id = student)

    mark = None
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark

    return render(request,'Student/view_result.html',{'result':result,'mark':mark})

