from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('shab',views.goto,name='shab')
]