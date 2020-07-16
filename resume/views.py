from django.shortcuts import render
from django.views import View
from .models import Resume

class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        context = {
            'resumes': resumes
        }
        return render(request, 'resumes.html', context)