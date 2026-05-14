from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('p/',EditView.as_view(),name='create'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('details/<int:id>/',DetailsView.as_view(),name='details')
]
