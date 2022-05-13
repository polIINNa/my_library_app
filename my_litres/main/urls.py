from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('abouttttt', views.about, name='about'),
    path('addbook', views.add, name='add')
]
