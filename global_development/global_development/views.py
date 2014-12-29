from django.shortcuts import render_to_response


def welcome_page(request):
    return render_to_response('welcome_page.html')


def signin(request):
    return render_to_response('signin.html')


def about(request):
    return render_to_response('welcome_about.html')


def contact(request):
    return render_to_response('contact.html')