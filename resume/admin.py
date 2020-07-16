from django.contrib import admin
from resume.models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'author')
    list_display_links = ('id', 'description', 'author')

admin.site.register(Resume, ResumeAdmin)

