from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from datetime import datetime
from .models import Album
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_protect

all_components = [
    'card',
    'carousel',
    'collapse',
    'manga',
    'gallery',
]

context = {
    'all_components': all_components,
}


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request,
                                     'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


@csrf_protect
def dashboard(request):
    # album = Album.objects.order_by('-list_date')

    album1 = [str(i) for i in list(range(1, 4))]
    album2 = [str(i) for i in list(range(1, 8))]

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UploadFileForm()

    this_context = {'all_components': all_components, 'form': form,
                    'album1': album1,'album2': album2}
    return render(request, 'accounts/dashboard.html', this_context)

@csrf_protect
def manage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage')
    else:
        form = UploadFileForm()

    this_context = {'all_components': all_components, 'form': form}

    return render(request, 'accounts/manage.html', this_context)
