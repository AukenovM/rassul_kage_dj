from django.urls import path
from snippets import views

urlpatterns = [
    path('<iin>/check-sex/', views.check_sex),
    path('<iin>/check-birthdate/', views.check_birthdate),
]
