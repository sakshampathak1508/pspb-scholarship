from django.urls import path

from .views import (
    AllScholarView,AllDataTabularFormView,UploadDocsView,CertificateView
)

urlpatterns = [
    path('all/', AllScholarView.as_view(),name="all scholars"),
    path('docs/', UploadDocsView.as_view(),name="Upload docs"),
    path('certs/', CertificateView.as_view(),name="Upload certificate"),
    path('data-table/', AllDataTabularFormView.as_view(),name="data-table"),
]