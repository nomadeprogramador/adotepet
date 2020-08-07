from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
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

def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'index/pet.html', {'pet':pet})

def logout_user(request):
    logout(request)
    return redirect('/login/')
def list_all_pet(request):
    pet=Pet.objects.filter(active=True)
    context={'pet':pet}
    return render(request,'index/list.html',context )


def list_user_pet(request):
    pet=Pet.objects.filter(active=True,user=request.user)
    return render(request,'index/list.html',{'pet':pet})

def register_pet(request):
    return render(request,'index/register.html')



@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    print(pet.id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/')



@login_required(login_url='/login/')
def set_pet(request):
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    user = request.user
    pet_id = request.POST.get('pet_id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.email = email
            pet.phone = phone
            pet.city = city
            pet.description = description 
            if file:
                pet.photo = file
            pet.save()
    else:
        pet = Pet.objects.create(email=email, phone=phone, city=city, description=description,
                                user=user, photo=file)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)