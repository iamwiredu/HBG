from django.urls import path
from .views import calc, bubble, slug, results


urlpatterns =[
    path('',calc,name='calcView'),
    path('bubble',bubble,name='bubble'),
    path('slug',slug,name='slug'),
    path('results',results,name='results')
]