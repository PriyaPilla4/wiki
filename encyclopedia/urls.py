from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/newpage", views.newpage, name="newpage"),
    path("wiki/savepage", views.savepage, name="savepage"),
    path("wiki/randompage", views.randompage, name="randompage"),
    path("wiki/save_edited_page", views.save_edited_page, name="save_edited_page"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.title, name="title")
    
    
]
