
from django.urls import path,include

# from.views import home

from app2 import views
urlpatterns = [
    # path('home/',home)        it show directly import
    path('home2/',views.home2)
]
