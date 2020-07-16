from django.contrib import admin
from vacancy.models import Vacancy

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'author')
    list_display_links = ('id', 'description', 'author')

admin.site.register(Vacancy, VacancyAdmin)

