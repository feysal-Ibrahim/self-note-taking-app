from django.conf.urls import url  # import the url function from the from the django.conf.urls
from . import views  # import the app's views module.
from django.conf import settings

urlpatterns=[
    url ( r'^$' , views.home , name='home' ) ,
]