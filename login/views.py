from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,  password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')

        else:
            messages.error(request,'Invalid Credentials.')
            return redirect('login')

    return render(request, 'login/loginpage.html')


def logoutuser(request):
    logout(request)
    return redirect('login')

