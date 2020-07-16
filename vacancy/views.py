from django.shortcuts import render
from django.views import View
from .models import Vacancy

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies
        }
        return render(request, 'vacancies.html', context)
