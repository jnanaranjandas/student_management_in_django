from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from stu_app.models import Course,SessionYear,CustomUser,Student,Staff,Subject,StaffNotification,StaffLeave,StaffFeedback,StudentNotification,StudentFeedback,StudentLeave,Attendance,Attendance_report
from django.contrib import messages



@login_required(login_url='/')
def Hod_home(request):

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

    return render(request,'Hod/myhome.html',context)


@login_required(login_url='/')
def AddStudent(request):
    course = Course.objects.all()
    session_year = SessionYear.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')


        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'Email is Already Exists')
            return redirect('add_stu')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exists')
            return redirect('add_stu')
        
        else :
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = '3',
            )

            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = SessionYear.objects.get(id = session_year_id)


            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender
            )
            student.save()
            messages.success(request,user.first_name +"  " + last_name + " Added Successfully")
            return redirect('add_stu')
        

    return render(request,'Hod/add_stu.html',{'course':course,'session_year':session_year})



@login_required(login_url='/')
def ViewStudent(request):
    student = Student.objects.all()

    return render(request,'Hod/view_stu.html',{'student':student})




@login_required(login_url='/')
def EditStudent(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = SessionYear.objects.all()
    return render(request,'Hod/edit_stu.html',{'student':student,'course':course,'session_year':session_year})




@login_required(login_url='/')
def UpdateStudent(request):
    if request.method == 'POST':
        stu_id = request.POST.get('stu_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id = stu_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password !='':
            user.set_password(password)
                
        if profile_pic != None and profile_pic !='':
            user.profile_pic = profile_pic

        user.save()    

        student = Student.objects.get(admin = stu_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = SessionYear.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record Updated Successfully')
        return redirect('view_stu')
    
    return render(request,'Hod/edit_stu.html')



@login_required(login_url='/')
def DeleteStudent(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('view_stu')



@login_required(login_url='/')
def AddCourse(request):
    if request.method == 'POST':
        course = request.POST.get('course_name')
        
        name = Course(name = course)
        name.save()
        messages.success(request,'Course Added Successfully')
        return redirect('add_course')

    return render(request,'Hod/add_course.html')



@login_required(login_url='/')
def ViewCourse(request):
    course = Course.objects.all()
    return render(request,'Hod/view_course.html',{'course':course})



@login_required(login_url='/')
def EditCourse(request,id):
    course = Course.objects.get(id = id)

    return render(request,'Hod/edit_course.html',{'course':course})



@login_required(login_url='/')
def UpdateCourse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request,'Course Updated Successfully')
        return redirect('view_course')

    return render(request,'Hod/edit_course.html')


@login_required(login_url='/')
def DeleteCourse(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course Deleted Successfully')
    return redirect('view_course')


@login_required(login_url='/')
def AddStaff(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exists')
            return redirect('add_staff')
        

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Email Already Exists')
            return redirect('add_staff')
        
        else :
            user = CustomUser(first_name=first_name,last_name=last_name,username=username,email=email,
                              profile_pic = profile_pic,user_type='2')
            user.set_password(password)
            user.save()

            staff = Staff(admin = user,address = address,gender=gender)
            staff.save()
            messages.success(request,'Staff Added Successfully')
            return redirect('add_staff')
        
    return render(request,'Hod/add_staff.html')


@login_required(login_url='/')
def ViewStaff(request):
    staff = Staff.objects.all()

    return render(request,'Hod/view_staff.html',{'staff':staff})


@login_required(login_url='/')
def EditStaff(request,id):
    staff = Staff.objects.get(id = id)

    return render(request,'Hod/edit_staff.html',{'staff':staff})


@login_required(login_url='/')
def UpdateStaff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id=staff_id)
        user.username=username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        
        if password != None and password !='':
            user.set_password(password)
                
        if profile_pic != None and profile_pic !='':
            user.profile_pic = profile_pic

        user.save()    

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,'Staff Updated Successfully')
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')
    


@login_required(login_url='/')
def DeleteStaff(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('view_staff')



@login_required(login_url='/')
def AddSubject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        sub_name = request.POST.get('sub_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name = sub_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request,'Subject Added Successfully')
        return redirect('add_sub')
    
    return render(request,'Hod/add_sub.html',{'course':course,'staff':staff})

@login_required(login_url='/')
def ViewSubject(request):
    subject = Subject.objects.all()

    return render(request,'Hod/view_sub.html',{'subject':subject})


@login_required(login_url='/')
def EditSubject(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()


    return render(request,'Hod/edit_sub.html',{'subject':subject,'course':course,'staff':staff})


@login_required(login_url='/')
def UpdateSubject(request):
    if request.method == 'POST':
        sub_id = request.POST.get('sub_id')
        sub_name = request.POST.get('sub_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        Subject.objects.filter(id=sub_id).update(
            name = sub_name,
            course = course,
            staff = staff
        )

        messages.success(request,'Subject Updated Successfully')
        return redirect('view_sub')



@login_required(login_url='/')
def DeleteSubject(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request,'Subject Deleted successfully')
    return redirect('view_sub')



@login_required(login_url='/')
def AddSession(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = SessionYear(session_start=session_start,session_end=session_end)
        session.save()
        messages.success(request,'Session Added Successfully')
        return redirect('add_session')

    return render(request,'Hod/add_session.html')



@login_required(login_url='/')
def ViewSession(request):
    session = SessionYear.objects.all()
    return render(request,'Hod/view_session.html',{'session':session})



@login_required(login_url='/')
def EditSession(request,id):
    session = SessionYear.objects.filter(id = id)
    return render(request,'Hod/edit_session.html',{'session':session})


@login_required(login_url='/')
def UpdateSession(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = SessionYear(
            id = session_id,
            session_start=session_start,
            session_end = session_end
        )
        session.save()
        messages.success(request,'Session Updated Successfully')
        return redirect('view_session')


@login_required(login_url='/')
def DeleteSession(request,id):
    session = SessionYear.objects.get(id = id)
    session.delete()
    messages.success(request,'Session Deleted Successfully')
    return redirect('view_session')



def Staff_Notification(request):
    staff = Staff.objects.all()
    see_notification = StaffNotification.objects.all().order_by('-id')[0:5]
    return render(request,'Hod/send_staff_notification.html',{'staff':staff,'see_notification':see_notification})



@login_required(login_url='/')
def SaveStaffNotification(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = StaffNotification(staff_id=staff,message=message)
        notification.save()
        messages.success(request,'Notification Send Successfully')
        return redirect('staff_notification')
    


@login_required(login_url='/')
def StaffLeaveView(request):
    staff_leave = StaffLeave.objects.all()

    return render(request,'Hod/staff_leave_view.html',{'staff_leave':staff_leave})



@login_required(login_url='/')
def StaffApprovedLeave(request,id):
    leave = StaffLeave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')



@login_required(login_url='/')
def StaffDisApprovedLeave(request,id):
    leave = StaffLeave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

    

def HodStaffFeedback(request):
    feedback = StaffFeedback.objects.all()
    feedback_history = StaffFeedback.objects.all().order_by('-id')[0:5]

    return render(request,'Hod/staff_feedback.html',{'feedback':feedback,'feedback_history':feedback_history})




def HodFeedbackSave(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = StaffFeedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
    
        return redirect('hod_staff_feedback')
    


def Student_Notification(request):
    student = Student.objects.all()
    notification = StudentNotification.objects.all()

    return render(request,'Hod/student_notification.html',{'student':student,'notification':notification})



def Student_Notification_Save(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin = student_id)
        stu_noti = StudentNotification(student_id = student,message=message)
        stu_noti.save()
        messages.success(request,'Notification Send Successfully')
        return redirect('student_notification')
    


def StudentFeedbackHod(request):
    feedback = StudentFeedback.objects.all()
    feedback_history = StudentFeedback.objects.all().order_by('-id')[0:5]

    return render(request,'Hod/stu_feedback_hod.html',{'feedback':feedback,'feedback_history':feedback_history})




def StudentFeedbackReply(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = StudentFeedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request,'Feedback Send Successfully')
        return redirect('stu_fedback_hod')
    

    
def StudentLeaveView(request):
    student_leave = StudentLeave.objects.all()

    return render(request,'Hod/student_leave_view.html',{'student_leave':student_leave})



@login_required(login_url='/')
def StudentApprovedLeave(request,id):
    student_leave = StudentLeave.objects.get(id = id)
    student_leave.status = 1
    student_leave.save()
    return redirect('stu_leave_view')



@login_required(login_url='/')
def StudentDisApprovedLeave(request,id):
    student_leave = StudentLeave.objects.get(id = id)
    student_leave.status = 2
    student_leave.save()
    return redirect('stu_leave_view')




def ViewStuAttendance(request):

    subject = Subject.objects.all()
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

    return render(request,'Hod/view_stu_attendance.html',{'subject':subject,'session_year':session_year,'action':action,'get_subject':get_subject,'get_session_year':get_session_year,'attendance_date':attendance_date,'attendance_report':attendance_report})

  