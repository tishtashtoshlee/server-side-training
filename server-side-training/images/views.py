import logging
import datetime

from mixpanel import Mixpanel

from django.contrib.auth import authenticate

from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.http import HttpResponseRedirect
from django.shortcuts import render

from images.forms import SignUpForm
from images.forms import LoginForm

logger = logging.getLogger('views.py')


def index(request):
    """Return the logged in page, or the logged out page
    """
    mp = Mixpanel("a28ae260bcb8356ddcbb5658e35cb787")

    print('Index view!')
    if request.user.is_authenticated():
        return render(request, 'images/index-logged-in.html', {
            'user': request.user
        })
    else:
        return render(request, 'images/index-logged-out.html')


def signup(request):
    """Render the Signup form or a process a signup
    """

    mp = Mixpanel("a28ae260bcb8356ddcbb5658e35cb787")
    
    print("hello101","natashalee")

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():

            form.save()
            id = form.cleaned_data.get('username')
            print("distinct_id",id)
            username = form.cleaned_data.get('first_name')
            print("first_name",username)
            lastname = form.cleaned_data.get('last_name')
            print("last_name",lastname)
            email = form.cleaned_data.get('email')
            print("email",email)

            mp.alias(email, id)
            print("Alias created for "+ email + " and distinct ID is " + id)

            now = datetime.datetime.now()
            mp.track(id, 'Signup', {
               'Username': username,
               'SignUp Date': now.isoformat()
            })
            print("SignUp Date",now.isoformat())
            mp.track(id, 'Page View', {
               'PageName': 'Signup Page',
               'SignUp PageView Date': now.isoformat()
            })
            mp.people_set(id, {
                '$name'    : username,
                '$last_name'     : lastname,
                '$email'         : email,
                'SignUpDate': now.isoformat()
            }, meta = {'$ignore_time' : 'true', '$ip' : 0})

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=id, password=raw_password)
            log_in(request, user)
            return HttpResponseRedirect('/')

    else:
        form = SignUpForm()

    return render(request, 'images/signup.html', {'form': form})


def login(request):
    """Render the login form or log in the user
    """
    mp = Mixpanel("a28ae260bcb8356ddcbb5658e35cb787")


    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            log_in(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'images/login.html', {
                'form': form,
                'error': 'Please try again'
            })
    else:
        form = LoginForm()
        return render(request, 'images/login.html', {'form': form})



def logout(request):
    """Logout the user
    """
    mp = Mixpanel("a28ae260bcb8356ddcbb5658e35cb787")
    
    log_out(request)
    return HttpResponseRedirect('/')
