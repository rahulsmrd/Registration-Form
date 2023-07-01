from django.shortcuts import render, HttpResponse, redirect
from home.forms import User_display, userProfileInfo
from home.models import username_list
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

user_logged_in = False

def index(request):
    return render(request, 'index.html')

context={'username':''}
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = User_display(request.POST)
        profile = userProfileInfo(request.POST)

        if user_form.is_valid and profile.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            # hashing the password by set_password method
            user.save()

            profile_form = profile.save(commit=False)

            # setting one to one relationship
            # this says that this profile info is related to user and that user is related to admins User
            profile_form.user = user

            if 'profile_pic' in request.FILES:
                profile_form.profile_pic = request.FILES['profile_pic']
            profile_form.save()
            registered = True
            return redirect("home:login")

        else:
            print(user_form.errors, profile.errors)
    else:
        user_form = User_display()
        profile = userProfileInfo()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                ins=username_list(username=username)
                ins.save()
                return redirect('home:index')
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone Tried to login and failed")

            print("Username: {} and password: {}".format(username, password))

            return HttpResponse("Invalid User Credentials")
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    username_list.objects.all().delete()
    return redirect(reverse("home:index"))


def dashboard(request):
    username=username_list.objects.values_list()
    if len(username):
        user_data=User.objects.values_list()
        user_data=user_data.filter(username=username[len(username)-1][1])
        context={"username":user_data[0][4],'first_name':user_data[0][5],'last_name':user_data[0][6],'email':user_data[0][7],}
        return render(request, 'dashboard.html', context)
    return render(request, 'dashboard.html')