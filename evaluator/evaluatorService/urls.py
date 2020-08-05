from django.urls import path
from django.conf.urls import url,include

from . import views
#from .views import end_game

urlpatterns=[
    path('evaluator/',views.getProjects,name="getProjects")
] 