from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from bookapp.models import Book
from bookapp.forms import BookForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    book=Book.objects.all()
    context={
        'book':book
        }
    return render(request,"home.html",context)
@login_required
def create(request):
   
   if request.method == "POST":
       title = request.POST.get('title')
       author_name=request.POST.get('author_name')
       description = request.POST.get('description')
       published_date= request.POST.get('published_date')
       book=Book(title=title,description=description,author_name=author_name,published_date=published_date)

       book.save()
       messages.warning(request,'Record has been added succesfully')
       return redirect('/home')
   
   return render(request,"createbook.html")

@login_required
def updatebook(request,id):
    book=Book.objects.get(id=id)
    
    if request.method == "POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid(): 
            form.save()
            messages.warning(request,'Record has been updated succesfully')
            return redirect('/home')
   
    return render(request,"update.html",{'book':book})

@login_required
def deletebook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    messages.warning(request,'book has been deleted')
    return redirect('/home')

def user_register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
             messages.warning(request,'Email already Exist')
             return redirect('/register/')
        else:

            user= User.objects.create_user(username=username,email=email,password=password)
            user.save
            messages.success(request,'User has been registered succesfully')
            return redirect('/login/')

    
    return render(request,"register.html")

def user_login(request):
   if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request,username=username,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.warning(request,'Username and password is incorrect')
            return redirect('login')
   return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect('/home/')