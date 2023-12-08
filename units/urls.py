from . import views

from django.urls import path

urlpatterns = [
    path('<str:unit_code>', views.unit_page, name="unit_page"),
    path('', views.unit_search, name="unit_search"),
]
