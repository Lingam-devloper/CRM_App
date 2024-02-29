from django.shortcuts import render,redirect
from . forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateForm


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Record
from django.contrib import messages

def home(request):
    return render(request,'web_app/index.html')

# Register form
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form':form}

    return render(request, 'web_app/register.html', context=context)

# login
def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
            messages.success(request,"You have logged")                

            return redirect("dashboard")

    context = {'form':form}

    return render(request , 'web_app/login.html', context=context)

#logout

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect("login")

#Dashboard
@login_required(login_url="login")
def dashboard(request):
    my_record=Record.objects.all()
    context={'records':my_record}
    return render(request,'web_app\dashboard.html',context=context)

# create a Record
@login_required(login_url='login')
def create_record(request):
    form=CreateRecordForm()
    if request.method=='POST':
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your record was created")
            return redirect('dashboard')
        
    context={"form":form}
    return render(request,"web_app/create_record.html",context=context)

#update record 
@login_required(login_url='login')

def update_record(request,id):
    record=Record.objects.get(id=id)
    form=UpdateForm(instance=record)
    if request.method=='POST':
        form=UpdateForm(request.POST,instance=record)
        if  form.is_valid():
            form.save()
            messages.success(request,"Your record was updated")
            return redirect ('dashboard')
    context={'form':form}
    return render(request,'web_app/update_record.html',context=context)

#view  single record
@login_required(login_url='login')
def  view_single_record(request,id):
    record=Record.objects.get(id=id)
    return render(request, 'web_app/view_record.html', {'record':record})

#delete record
@login_required(login_url='login')
def  delete_record(request,id):
    record=Record.objects.get(id=id)
    record.delete()
    messages.success(request,"Your record was  deleted")
    return redirect('dashboard')