from django.urls import path
from menu.views import menu


urlpatterns = [
    path('', menu, name='tags')
]
