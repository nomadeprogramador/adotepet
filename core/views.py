from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet
# Create your views here.
@csrf_protect
@login_required(login_url='/login/')
def index(request):
    return render(request,'index/index.html')
def login_user(request):
    return render (request,'index/login.html')
def submit_login(request):
    if request.POST:
        username=request.POST.get('username')
        passoword=request.POST.get('password')
        print(username)
        print(passoword)
        user=authenticate(username='username',passoword='password')
        if user is not None:
            login(request,user)
            return redirect('/login/#')
        else:
            messages.error(request,'Senha errada ou login errado')
            return redirect ('/login/')
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'User/Passowrd WRONG, Please Try again')
    return redirect('/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')
def list_all_pet(request):
    pet=Pet.objects.filter(active=True)
    print(pet.query)
    context={'pet':pet}
    return render(request,'index/list.html',context )
def list_user_pet(request):
    pet=Pet.objects.filter(active=True,user=request.user)
    return render(request,'index/list.html',{'pet':pet})

def pet_detail(request,id):
    pass 