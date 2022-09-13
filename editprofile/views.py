from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.formats import EditProfile, EditUser
from django.contrib.auth.decorators import login_required
from home.models import Profile


@login_required
def profileuser(request, user_id):
    userprofile = Profile.objects.all()
    userid = User.objects.get(id=user_id)
    if request.method == 'POST':
        user_form = EditUser(request.POST, instance=request.user)
        profile_form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')

    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=request.user.profile)

    return render(request, 'editprofile/editprofilepage.html', {'user_form': user_form, 'profile_form': profile_form, 'userprofile':userprofile})



