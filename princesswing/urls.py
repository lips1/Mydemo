
from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [ 


path('myarea/', views.myarea, name='myarea'),
path('homepage1/', views.homepage1, name='homepage1'),
path('signincall/', views.signincall, name='signincall'),
path('myareacall/', views.myareacall, name='myareacall'),
]


