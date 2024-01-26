from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    users = User.objects.exclude(username = request.user.username)
    return render(request,'core/index.html',{'users':users})