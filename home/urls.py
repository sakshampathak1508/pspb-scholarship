from django.urls import path

from .views import (
    AllScholarView,AllDataTabularFormView
)

urlpatterns = [
    path('all/', AllScholarView.as_view(),name="all scholars"),
    path('data-table/', AllDataTabularFormView.as_view(),name="data-table"),
]