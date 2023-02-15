from tableauAcceuil import views
from django.urls import path
from django.conf import settings
from tableauAcceuil.views import base_view
from tableauAcceuil.views import home_view

urlpatterns = [
    path('base/', views.base_view),
    path('home/', views.home_view),
]