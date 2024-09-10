from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chat.models import Hotel
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    hoteles =Hotel.objects.all()
    if request.method=='GET':
        st=request.GET.get('sear')
        if st!=None:
            hoteles = Hotel.objects.filter(check_in__icontains=st)
    context={
        'hoteles':hoteles
    }
    
    return render (request,'index.html',context)

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def hotels(request):
    hoteles =Hotel.objects.all()
    if request.method=='GET':
        st=request.GET.get('inputsearch')
        if st!=None:
            hoteles = Hotel.objects.filter(hotel_name__icontains=st)
    context={
        'hoteles':hoteles
    }
    return render(request,'hotels.html',context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')