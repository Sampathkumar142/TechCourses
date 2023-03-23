from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.UserQuery)

@admin.register(models.Courses)
class CourseAdmin(admin.ModelAdmin):
    ordering =['title']
    search_fields = ['title__isstartswith']