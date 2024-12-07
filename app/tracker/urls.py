from django.urls import path
from .views import *

urlpatterns = [
    path('track/', track_click, name='track_click'),
    path('thank-you/<slug:project>/', thank_you, name='thank_you'),
]