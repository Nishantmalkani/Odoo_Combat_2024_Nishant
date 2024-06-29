from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import *

from .models import *

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import check_password


# Create your views here.

def register(request):
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user_info = Facultydetail.objects.get(email=email)
            if user_info.password == password:
                request.session['user_login'] = email
                user = request.session['user_login']
                return redirect('dashboard')
        except:
            return render(request, 'login')
    else:
        return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
