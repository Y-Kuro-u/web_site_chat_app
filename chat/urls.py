from django.urls import path
from chat.views.test_view import test

urlpatterns = [
    path('', test, name='index'),
]