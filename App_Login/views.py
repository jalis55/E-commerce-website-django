from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

# authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# forms and models
from App_Login.models import Profile
from App_Login.forms import ProfileForm,UserForm


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
            return HttpResponseRedirect(reverse('App_Login:user_login'))
        
    return render(request,'App_Login/signup.html',context=context)


def user_login(request):
    form=AuthenticationForm
    context={"form":form}

    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username,password)

            if user is not None:
                login(request,user)
                return HttpResponse("authenticate")
    return render(request,'App_Login/login.html',context=context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("logged out")

@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)

    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            form=ProfileForm(instance=profile)
    return render(request,'App_Login/change_profile.html',context={'form':form})
