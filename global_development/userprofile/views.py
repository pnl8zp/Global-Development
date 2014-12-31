from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_welcome(request):
    return render_to_response('dashboard_welcome.html')


@login_required
def dashboard_overview(request):
    return render_to_response('dashboard_overview.html')


@login_required
def dashboard_resources(request):
    return render_to_response('dashboard_resources.html')


@login_required
def profile(request):

    args = {}
    args['user'] = request.user
    args['profile'] = request.user.profile

    return render_to_response('profile.html', args)


@login_required
def dashboard_map(request):
    return render_to_response('dashboard_map.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/profile/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('profile_form.html', args)
