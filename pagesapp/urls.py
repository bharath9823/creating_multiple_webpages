from django.urls import path
from pagesapp import views

urlpatterns=[
    path('',views.index),
    path('second/',views.second),
    path('third/',views.third)
]