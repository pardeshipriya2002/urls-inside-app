
from django.urls import path,include

# from.views import home

from app import views
urlpatterns = [
    # path('home/',home)        it show directly import
    path('home/',views.home)
]
