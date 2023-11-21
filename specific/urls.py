from specific.views import *
from django.urls import path
app_name="specific"
urlpatterns=[
    path("nz/",nz,name="nz")
]