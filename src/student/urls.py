from django.urls import path
from .views import studentFormView

urlpatterns = [
    path('', studentFormView, name = 'studentForm')
]