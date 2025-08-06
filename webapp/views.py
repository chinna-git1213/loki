from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.models import User
from webapp.models import UserProfile,form_email

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.conf import settings

from twilio.rest import Client

def home(request):
    context={}
    
    return render(request,'home.html',context)



def admin_login(request):
    context={}
    return render(request,'admin/admin_login.html',context)

def emp_register(request):
    latest_user = User.objects.latest('date_joined')  # Get the most recent user
    
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        pic = request.FILES['pic']

        

        
    
        p=latest_user.password

        if User.objects.filter(username=email).exists():
            messages.error(request, "Username already taken! Try another.")
            return redirect('emp_register')

        user = User.objects.create(username=email,email=email,first_name=name,password=p)
        
        print('its done_1')
        data = UserProfile.objects.create(user=user,profile_picture=pic,phone_number=phone,age=age)
        user.save()
        data.save()
        return redirect('emp_login')
    e=latest_user.email
    context={'email':e}
    return render(request,'admin/emp_register.html',context)


def emp_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'admin/emp_login.html')

@login_required
def dashboard(request):
    a= User.objects.all()
    print(a)
    profile = UserProfile.objects.get(user=request.user)
    card = form_email.objects.all()
    context = {'profile': profile,'card':card}
    return render(request, 'admin/dashboard.html', context)

def emp_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('emp_login')

@login_required
def email_form(request):
    profile = UserProfile.objects.get(user=request.user)
    context = {'profile': profile}
    if request.method=="POST":
        f_email = request.user
        to_email =request.POST['email_t']
        c_email = request.POST['email_c']
        sub = request.POST['subject']
        body = request.POST['body']
        password = request.POST['password']
        pdf = request.FILES['file']
        phone=request.POST['phone']

        from django.core.mail import EmailMessage


        email = EmailMessage(
            subject=sub,
            body=body,
            from_email="dummydata1543@gmail.com",
            to=["yogeshjanakiraman52@gmail.com","g.subramaniyam2003@gmail.com"],
        )

        
                
        email.send()


        print("Email Sent Successfully!")

        

        account_sid = 'AC6d3e5e0f3e39a640b344917d9eede195'
        auth_token = '30b845c87be6144dc3739efeae21f116'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='+15139607872',
        body=password,
        to='+919345626618'
        )

        print(message.sid)
        print("Message SID:", message.sid)

    
        print( message.sid)

        print('success')

        user=form_email.objects.create(user=f_email,email_ids=c_email,t_email=to_email,subject=sub,body=body,pdfs=pdf,password=password)
        user.save()
        return redirect('dashboard')



    return render(request,'admin/email_form.html',context)


