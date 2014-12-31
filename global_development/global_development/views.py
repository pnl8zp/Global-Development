from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from forms import SigninForm


def welcome_page(request):
    return render_to_response('welcome_page.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponse('Account is inactive')
        else:
            return HttpResponse('Account Does Not exist')

    args = {}
    args.update(csrf(request))

    args['form'] = SigninForm()

    return render_to_response('signin.html', args)


def signup(request):
    return render_to_response('signup.html')


def about(request):
    return render_to_response('welcome_about.html')


def contact(request):
    return render_to_response('contact.html')


def signout(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')