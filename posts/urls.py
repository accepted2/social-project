from django.urls import path, include
from . import views

urlpatterns = [
    path("posts/", views.post, name="post"),
    path("edit_post/<str:pk>/", views.edit_post, name="edit_post"),
    path("delete_post/<str:pk>/", views.delete_post, name="delete_post"),
]
