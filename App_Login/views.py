from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

# authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login,logout,authenticate

# forms and models
from App_Login.models import Profile
from App_Login.forms import ProfileForm,UserForm

# messages
from django.contrib import messages


# Create your views here.
def sign_up(request):
    form=UserForm
    context={
        "form":form,
    }
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account has created successfully")
            return HttpResponseRedirect(reverse('App_Login:user_login'))
    
    context={
        "form":form,
        
    }
        
    return render(request,'App_Login/signup.html',context=context)


def user_login(request):
    form=AuthenticationForm
    context={"form":form}

    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username=username,password=password)

            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request,'App_Login/login.html',context=context)


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You have logged out")
    return HttpResponseRedirect(reverse('App_Shome:home'))

@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)

    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"profile has updated successfully")
            form=ProfileForm(instance=profile)
    return render(request,'App_Login/change_profile.html',context={'form':form})
