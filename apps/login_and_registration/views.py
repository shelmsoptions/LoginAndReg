from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

def user_in_session(request):
    if 'user' in request.session:
        print 'method - user in sessions True!!'
        return True
    else:
        print 'method - user in sessions False!!'
        return False

def index(request):
    if user_in_session(request):
        print 'index - user in session = True'
        # VV  this is where to plug-in the app  VV   *****
        return render(request, 'login_and_registration/login.html')
    # context = {
    #
    # }
    return render(request, 'login_and_registration/login.html')

def register_login(request):
    # if request.method == 'POST':
    if request.POST['action'] == 'register':
        result = User.objects.reg_validation(request)
    elif request.POST['action'] == 'login':
        result = User.objects.login_validation(request)
    if result[0] == False:
        print 'logged-in? False - incorrect data'
        request.session['errors'] = result[1]
        context = {
            'errors': request.session['errors'],
        }
        # print 'errors from register_login method view: ', errors
        return render(request, 'login_and_registration/login.html', context)
    print result[1]
    return login_user(request, result[1])


def login_user(request, user):
    print user
    request.session['user'] = {
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # 'errors': errors,
    }
    # print request.session['user']
    # context = {
    #     'user_id': user.id,
    #     'first_name': user.first_name,
    #     'last_name': user.last_name,
    #     # 'errors': errors,
    # }

    # VV  this is where to plug-in the app  VV   *****
    # return render(request, 'login_and_registration/home.html')
    return redirect('LogReg:home')

def home(request):
    return render(request, 'login_and_registration/home.html')

def delete(request):
    pass

def logout(request):
    request.session.clear()
    return render(request, 'login_and_registration/login.html')