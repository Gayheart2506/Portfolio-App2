from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path("", views.index, name="proj_page"),
    path("<int:pk>", views.detail_page, name="details")
]