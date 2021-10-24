from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExperienceList.as_view(), name='experience'),
    path('jobs/', views.JobsList.as_view(), name='jobs')

]
