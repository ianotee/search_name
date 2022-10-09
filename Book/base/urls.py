from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
      path( '',views.home, name='home'),
       path( 'nav/',views.nav, name='nav'),
      path( 'base/',views.base, name='base'),
]
