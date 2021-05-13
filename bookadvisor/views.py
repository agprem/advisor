from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login,authenticate,logout
from bookadvisor.forms import RegistrationForm,CustomUserAuthenticationForm,Advisorform
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import check_password
import datetime


#HOME PAGE----------------------------------------------------------
# Create your views here.
def homepage(request):
    return render(request,'home.html')

#----------------- ADVISOR PART-------------------------------------------------------------------------------------------


# CODE FOR CREATING ADVISOR--------------------------------------------
def createadvisor(request):
    context={}
    if request.POST:
        #print("INside POST")
        form = Advisorform(request.POST,request.FILES)
        #print("hello")
        if form.is_valid():
            #print("Form valid")
            form.save()
            context['info']=form
            return render(request,"advisorcreated.html",context)
        else:
            #print("ELSE:")
            return render(request,"advisor.html",{'form':form})

    else:
        form = Advisorform()
        print("Not POST")
        return render(request,'advisor.html', {'form' : form})



# CODE FOR SHOWING ALL ADVISORS AFTER USER LOGINS --------------------------------------------------
def bookadvisor(request):
    user1=Advisor.objects.all()
    print("Book",user1)
    return render(request,'bookadvisor.html',{'user1':user1})


#CODE FOR BOOKING ADVISORS-----------------------------------
def booking(request,id):
    context={}
    advisor=Advisor.objects.get(id=id)
    #print("*****",advisor.bid)
    if (advisor.bid==None):
        #print(advisor.bid)
        advisor.bid=advisor.id
        advisor.bookingtime=datetime.datetime.now()

        #print("Booking---->",advisor.bid,advisor.bookingtime)
    #user=Advisor(bid=advisor.bid,bookingtime=advisor.bookingtime)
        advisor.save()
    #print(advisor.first_name)
        context['info']=advisor
        return render(request,'bookingdone.html',context)
    else:
        return HttpResponse("<br><br><h2>Advisor Booked already Try later...</h2>")




#CODE FOR SHOWING ALL BOOKED ADVISORS----------
def showbooked(request):
    #print("hello in booked")
    context={}
    #ad=Advisor.objects.all()
    #print("********",ad.id)
    advisor=Advisor.objects.exclude(bid__isnull=True)
    #print(advisor,advisor.first_name)
    #print("inside if",advisor)
    context['advisors']=advisor
    return render(request,"bookedpage.html",context)



#-------------------------- USER PART-------------------------------------------------------------------------------------------


#CODE FOR REGISTERING USER---------------------------------------------
def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            pw=user.password
            #print("Email",email,"Password",password)
            #email = form.cleaned_data.get("email")
            #raw_password = form.cleaned_data.get('password')
            user.set_password(pw)
            user.save()
            #print("fff",pw)
            #user = auth.authenticate(email=email,password=raw_password)
            #print("Helllllll",user,email,raw_password)
            #print(user.name)
            #login(request,user)
            #print("gggggg---------",user)
            context['user']=user
            return render(request,"home.html",context)
        else:
            context['registration_form']=form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'register.html',context)


#CODE FOR LOGIN THE USER TO SEE ADVISORS LIST-------
def login_view(request):
    context={}
    if request.POST:
        #print("inside post")
        form = CustomUserAuthenticationForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        #print("outside Valid")
        user = auth.authenticate(email = email, password= password)
        #print("After authenticate")
        #print("user",user)
        #print("UID",user.id)
        #uid=user.id
        #print("Type",type(uid))
        #print(uid)
        if user:
            context[user]=user
            return redirect("/user/userid/advisor",context)
    else:
        #print("In else")
        form = CustomUserAuthenticationForm()
    context['login_form'] = form
    return render(request,'login.html',context)




#CODE FOR LOGOUT
def logout_view(request):
    logout(request)
    return redirect('/')
