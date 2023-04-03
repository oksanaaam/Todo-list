from django.urls import path
from case.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "case"
