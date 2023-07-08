from django.contrib import admin
from django.urls import path
import main.urls
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.views.index),
    path("map/", main.views.map, name="map"),
]
