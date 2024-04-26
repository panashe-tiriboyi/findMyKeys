from django.urls import path, include
from . import views
# from .views import HelloWorldView


urlpatterns = [
    # path('home/', views.home),
    # path('helloworld/', views.hello_world),
    # path('hello/', HelloWorldView.as_view(), name='hello-world'),
    # path('email/', views.email, name='email'),
     path('cordinates/', views.cordinates, name='cordinates'),
]

