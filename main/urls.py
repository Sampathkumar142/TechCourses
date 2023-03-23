from django.urls import path
from . import  views
from django.views.generic import TemplateView



urlpatterns = [
    path('',TemplateView.as_view(template_name='base/home.html')),
    path('home/',views.getHome),
    path('about/',views.about),
    path('contact/',views.UserQueryForm),
    path('courses/',views.courses),

]