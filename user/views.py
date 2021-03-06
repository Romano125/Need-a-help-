from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import (
    UserRegisterForm,
    ProfileRegisterForm,
    UserUpdateForm,
    RepairmanUpdateForm,
    ClientUpdateForm
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ClientNotifications, RepairmanNotifications
from need_a_help import settings
from user.models import ClientMessage


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form_p = ProfileRegisterForm(request.POST)
        if form.is_valid() and form_p.is_valid():
            user = form.save()
            user.profile.address = form_p.cleaned_data.get('address')
            user.profile.birth_date = form_p.cleaned_data.get('birth_date')
            user.profile.role = form_p.cleaned_data.get('role')
            user.profile.gender = form_p.cleaned_data.get('gender')

            user.profile.user_description = f'An repairman whose profession is Other, Master Other — wide range of knowladges based on his profession, can help with similar types of job which contains part of his own profession, Newby - still we don\'t have any information about his past jobs and expiriences...'

            user.profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        form_p = ProfileRegisterForm()

    context = {
        'form': form,
        'form_p': form_p,
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }

    return render(request, 'user/register.html', context)


def login_success(request):
    if request.user.profile.role == 'client':
        return redirect("main_client")
    else:
        return redirect("main_repairman")


@login_required  # decorator dodaje funkcionalnost nasoj funkciji
def profile(request, log):
    user = User.objects.filter(id=log).first()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if user.profile.role == 'repairman':
            p_form = RepairmanUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        else:
            p_form = ClientUpdateForm(request.POST,
                                      request.FILES,
                                      instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have updated your account!')
            return redirect('profile', log=user.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        if user.profile.role == 'repairman':
            p_form = RepairmanUpdateForm(instance=request.user.profile)
        else:
            p_form = ClientUpdateForm(instance=request.user.profile)

    us = request.user
    not_r = RepairmanNotifications.objects.filter(repairman=us, remove=False).order_by('-date')
    not_c = ClientNotifications.objects.filter(client=us, remove=False).order_by('-date')
    not_rep = RepairmanNotifications.objects.filter(repairman=user, seen=False).count()
    not_cli = ClientNotifications.objects.filter(client=user, seen=False).count()
    mess_cli = ClientMessage.objects.filter((Q(client=us) | Q(sender=us)) & Q(seen=False)).order_by("-date")
    mess_cli_c = ClientMessage.objects.filter(Q(client=us) & Q(seen_notif=False)).count()

    args = {
        'u_form': u_form,
        'p_form': p_form,
        'not_c': not_c,
        'not_r': not_r,
        'not_cli': not_cli,
        'not_rep': not_rep,
        'mess_cli': mess_cli,
        'mess_cli_c': mess_cli_c,
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }

    return render(request, 'user/profile.html', args)
