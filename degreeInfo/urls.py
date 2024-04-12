from .views import unit_page, hx_unit_search, unit_search, degree_plan, hx_degree_plan

from django.urls import path

urlpatterns = [
    path('degreeplan', hx_degree_plan, name="degree_plan"),
    path('units/<str:unit_code>', unit_page, name="unit_page"),
    path('units', hx_unit_search, name="unit_search"),
]
