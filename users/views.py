from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views import View
from users.forms import NewForm
from django.contrib.auth.models import User
from vacancy.models import Vacancy
from resume.models import Resume
from django.core.exceptions import PermissionDenied

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        auth = request.user.is_authenticated
        user = request.user
        content_vacancy = Vacancy.objects.all().filter(author=user)
        content_resume = Resume.objects.all().filter(author=user)
        if auth:
            if request.user.is_staff:
                context = {
                    'content': content_vacancy,
                    'user': user
                }
            else:
                context ={
                    'content': content_resume,
                    'user': user
                }
        return render(request, 'home.html', context)

class NewVacancy(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif not request.user.is_staff:
            raise PermissionDenied
        elif request.user.is_staff:
            form = NewForm(request.POST)
            user = request.user
            title = 'Vacancy'
            context ={
                'form': form,
                'user': user,
                'title': title
            }
        return render(request, 'new.html', context)
    
    def post(self, request, *args, **kwargs):
        auth = request.user.is_authenticated
        description = request.POST['description']
        author = request.user
        if auth:
            if request.user.is_staff:
                Vacancy.objects.create(author=author, description=description)
        else:
            raise PermissionDenied
        return redirect('home')

class NewResume(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied
        if not request.user.is_authenticated:
            raise PermissionDenied
        form = NewForm(request.POST)
        user = request.user
        title = 'Resume'
        context ={
            'form': form,
            'user': user,
            'title': title
        }
        return render(request, 'new.html', context)
    
    def post(self, request, *args, **kwargs):
        auth = request.user.is_authenticated
        description = request.POST['description']
        author = request.user
        if auth:
            if not request.user.is_staff:
                Resume.objects.create(author=author, description=description)
        else:
            raise PermissionDenied
        return redirect('home')