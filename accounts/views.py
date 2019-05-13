from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout, models
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
# Create your views here.


def Login(request):
    if( request.user.is_authenticated ):
        return redirect('/')
    message = ''
    if( request.method =='POST'):
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = uname, password = password)
        if( user is not None ):
            login(request, user)
            return redirect('/')
        else:
            message = 'Invalid Username Or Password'
    content = {
        'form': LoginForm(),
        'message': message,
    }
    return render(request, 'accounts/login.html', content)


def signup(request):
    if( request.user.is_authenticated ):
        return redirect('/')
        
    if( request.method == 'POST'):
        form = SignUpForm(request.POST)
        if( form.is_valid() ):
            instance, flag = models.User.objects.get_or_create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            instance.set_password(form.cleaned_data['password1'])
            instance.save()
            if(flag):
                Profile.objects.create(
                    user= instance,
                    shopOwner = form.cleaned_data['shopOwner'],
                )
            user = authenticate(request, username = instance.username, password = form.cleaned_data['password1'])
            login(request, user)
            # If shopkeeper then
            if(form.cleaned_data['shopOwner']):
                return redirect('/shophome/')
            # If user then -- (make)
            else:
                return redirect('/userhome/')

    else:
        form = SignUpForm()
    
    content = {
        'form': form
    }
    return render(request, 'accounts/signup.html', content)

@login_required
def Logout(request):
    logout(request)
    content = {
        'message': 'You have been logged out!'
    }
    return render(request, 'message.html', content)