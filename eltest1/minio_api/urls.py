from django.urls import path
from minio_api.views import upload

urlpatterns = [
    path('',upload,name='upload')
]