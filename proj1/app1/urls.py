from django.urls import path
from . import views

urlpatterns=[
    path('show',views.search,name='show')
]