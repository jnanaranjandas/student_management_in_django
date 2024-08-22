from django.shortcuts import render,redirect,HttpResponse
from stu_app.emailbackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stu_app.models import CustomUser
# Create your views here.

def base(request):
    return render(request,'base.html')

def user_login(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,
                                         username=request.POST.get('email'),password = request.POST.get('password'))
        if user != None :
            login(request,user)
            user_type = user.user_type

            if user_type == '1':
               return redirect('home')

            elif user_type == '2':
               return redirect('staff_home')

            elif user_type == '3':
               return redirect('student_home')

            else:
                messages.error(request,'Email and Password Are Invaild')
                return redirect('login')
    else:
        messages.error(request,'Email and Password Are Invaild')
        return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'user':user})


def ProfileUpdate(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            
          
            if password != None and password !='':
                customuser.set_password(password)

                
            if profile_pic != None and profile_pic !='':
                customuser.profile_pic = profile_pic
                
            
            customuser.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')

        except:    
            messages.error(request,'Update Your Profile Again')


    return render(request,'profile.html')





