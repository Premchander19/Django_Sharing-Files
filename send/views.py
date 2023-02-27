from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Data
from django.contrib.auth.models import User, auth
import datetime

# Create your views here.

main_name = None


def home(request):
    return render(request, 'home.html')


def send(request):
    if request.method == 'POST':
        check = User.objects.all()
        for user_check in check:
            if user_check.is_superuser == 0:
                expired = datetime.timedelta(minutes=30)
                if user_check.date_joined + expired < datetime.datetime.now():
                    delete_username = user_check.username
                    user_check.delete()
                    file_object = Data.objects.filter(username=delete_username)
                    file_object.delete()
        username = request.POST['name']
        name = '{}_send/receive'.format(username)
        try:
            if User.objects.get(username=name):
                messages.error(request, 'Username Already Taken')
                return redirect('send')
        except:
            globals()['main_name'] = name
            passwd = 'send/receive'
            create = User.objects.create_user(username=name, password=passwd)
            create.save()
            users = auth.authenticate(username=name, password=passwd)
            if users is not None:
                auth.login(request, users)
                return redirect('upload')
    else:
        return render(request, 'user.html')


def receive(request):
    if request.method == 'POST':
        username = request.POST['name']
        name = '{}_send/receive'.format(username)
        #globals()['main_name'] = name
        passwd = 'send/receive'
        user = auth.authenticate(username=name, password=passwd)
        if user is not None:
            auth.login(request, user)
            return redirect('download')
        else:
            messages.error(request, 'Wrong UserName')
            return redirect('receive')

    else:
        return render(request, 'user.html')


# @login_required(login_url='receive')
def download(request):
    if request.user.is_authenticated:
        user = Data.objects.filter(username=request.user.username)
        auth.logout(request)
        return render(request, 'download.html', {'downl': user})
    else:
        messages.error(request, 'Enter Username First')
        return redirect('receive')


def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            for i in request.FILES.getlist('file'):
                data = Data()
                data.username = globals()['main_name']
                data.file = i
                data.text = i
                now = datetime.datetime.now()
                time = now.strftime("%H:%M")
                data.Time = time
                new = datetime.timedelta(minutes=30)
                expired = now + new
                data.Expired = expired.strftime("%H:%M")
                data.save()
                auth.logout(request)
            return redirect('/')
        else:
            user = request.user.username
            username, default = user.split('_')
            return render(request, 'upload.html', {'username': username})
    else:
        messages.error(request, 'Enter Username First')
        return redirect('send')
