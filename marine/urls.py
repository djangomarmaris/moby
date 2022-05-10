from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'marine'


urlpatterns =[
    path('',views.index,name ='index'),
    path('about/',views.about,name='about'),
    path('istec/',views.istec,name='istec'),
    path('contact/',views.contact,name='contact'),
]
