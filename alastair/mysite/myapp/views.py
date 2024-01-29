from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from .utils import send_email_to_client
# Create your views here.
def register_user(request):
    
    if request.method == 'POST':
        user_details = UserForm(request.POST)
        if user_details.is_valid():
            user_details.save()
            send_email_to_client()
            return redirect('login')
    else :
        user_details = UserForm()
    return render(request,'index1.html',{'form' : user_details})

def login_user(request):
    if request.method == 'POST':
        user_details = UserForm(request.POST)
        
        #db_user = User.objects.filter(user_email = request.POST['user_email'])
        print(request.POST)
        user_found = User.objects.get(user_email = request.POST['user_email'])
        if request.POST['user_password'] == user_found.user_password:
            return HttpResponse("success")
        else :
            return HttpResponse("failure")
    else :
        user_details = UserForm()
    return render(request,'index2.html',{'form' : user_details})
