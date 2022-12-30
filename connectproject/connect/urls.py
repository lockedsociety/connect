from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="connect-index"),
    path("profile/", views.profile, name="connect-profile"),
    path("profile/<str:username>", views.individual_profile, name="connect-individual_profile"),
    path("about/", views.about, name="connect-about"),
]