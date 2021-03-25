from django.urls import path
from severity_grading import views as dr_grading_views

urlpatterns = [
    path('', dr_grading_views.dr_dme_grading, name="dr_grade_analysis"),
]
