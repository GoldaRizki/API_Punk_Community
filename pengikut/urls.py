# todo/todo_api/urls.py : API urls.py
#from django.conf.urls import url
from django.urls import path, include
from .views import (
    PengikutApiView,
    KuantumAPI
    )

urlpatterns = [
    path('api/', PengikutApiView.as_view()),
    path('api/quantum/', KuantumAPI.as_view()),
]