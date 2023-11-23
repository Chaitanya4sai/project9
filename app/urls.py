from app.views import *

from django.urls import path

app_name='india'

urlpatterns=[

    path('sai/',sai,name='sai')
]