
from django.urls import path,include

# from.views import home

from app1 import views
urlpatterns = [
    # path('home/',home)        it show directly import
    path('home1/',views.home1)
]
