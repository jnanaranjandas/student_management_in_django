from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *



@login_required(login_url='/')
def Home(request):

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
    return render(request,'Staff/home.html',context)



@login_required(login_url='/')
def Notification(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        notification = StaffNotification.objects.filter(staff_id=staff_id)


    return render(request,'Staff/notification.html',{'notification':notification})    


@login_required(login_url='/')
def Staff_Mark_Notification(request,status):
    notification = StaffNotification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')


@login_required(login_url='/')
def ApplyLeave(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = StaffLeave.objects.filter(staff_id = staff_id)
    return render(request,'Staff/apply_leave.html',{'staff_leave_history':staff_leave_history})


@login_required(login_url='/')
def ApplyLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin = request.user.id)

        leave = StaffLeave(
            staff_id = staff,
            data =  leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request,'Leave Successfully Sent')
        return redirect('apply_leave')
    


def  Staff_Feedback(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history = StaffFeedback.objects.filter(staff_id = staff_id)

    return render(request,'Staff/staff_feedback.html',{'feedback_history':feedback_history})



def Staff_Feedback_Save(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)

        feedback = StaffFeedback(staff_id = staff,feedback=feedback,feedback_reply = "")
        feedback.save()
        messages.success(request,'Feedback Send Successfully')
        return redirect('send_feedback')
    



def StaffTakeAttendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff_id)
    session_year = SessionYear.objects.all()

    action = request.GET.get('action')
    
    students = None
    get_subject = None
    get_session_year = None

    if action is not None :
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = SessionYear.objects.get(id = session_year_id)
            subject = Subject.objects.filter(id = subject_id)

            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)
    
    return render(request,'Staff/take_attendance.html',{'subject':subject,'session_year':session_year,'get_subject':get_subject,'get_session_year':get_session_year,'action':action,'students':students})




def StaffSaveAttendance(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject =  get_subject = Subject.objects.get(id = subject_id)
        get_session_year = SessionYear.objects.get(id = session_year_id)

        atten = Attendance(
            subject_id = get_subject,
            attendance_data = attendance_date,
            session_year_id = get_session_year
        )
        atten.save()

        for i in student_id :
            stu_id = i
            int_stu = int(stu_id)

            present_stu = Student.objects.get(id = int_stu)

            atten_report = Attendance_report(
                student_id = present_stu,
                attendance_id = atten,
            )
            atten_report.save()
           

    return redirect('staff_take_attendance')




def ViewAttendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = SessionYear.objects.all()

    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None


    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = SessionYear.objects.get(id = session_year_id)

            attendance = Attendance.objects.filter(subject_id = get_subject,attendance_data = attendance_date)
            for i in attendance :
                attendance_id = i.id
                attendance_report = Attendance_report.objects.filter(attendance_id = attendance_id)

    return render(request,'Staff/view_attendance.html',{'subject':subject,'session_year':session_year,'action':action,'get_subject':get_subject,'get_session_year':get_session_year,'attendance_date':attendance_date,'attendance_report':attendance_report})


def StaffAddResult(request):
    staff = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff_id = staff)

    session_year = SessionYear.objects.all()
    action = request.GET.get('action')

    get_subject  = None
    get_session = None
    students = None

    if action is not None :
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = SessionYear.objects.get(id = session_year_id)

            subjects = Subject.objects.filter(id = subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)



    return render(request,'Staff/add_result.html',{'subjects':subjects,'session_year':session_year,'action':action,'get_subject':get_subject,'get_session':get_session,'students':students})



def StaffSaveResult(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)

        check_exists = StudentResult.objects.filter(subject_id = get_subject,student_id = get_student).exists()

        if check_exists :
            result = StudentResult.objects.get(subject_id = get_student,student_id = get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request,'Successfully updated')
            return redirect('staff_view_attendance')

        else :
            result = StudentResult(student_id = get_student,subject_id = get_subject,
                                   exam_mark = exam_mark,assignment_mark = assignment_mark)
            result.save()
            messages.success(request,'Result Added Successfully')
            return redirect('staff_view_attendance')
   


















