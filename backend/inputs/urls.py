from django.urls import path
from django import urls
from .views import LabelDetail, LabelList, DocumentDetail, DocumentList, helloWorld

urlpatterns = [
    path('labels/', LabelList.as_view(), name="Labels"),
    path('label/<int:pk>', LabelDetail.as_view(), name="Label"),
    path('documents/', DocumentList.as_view(), name="Documents"),
    path('document/<int:pk>', DocumentDetail.as_view(), name="Document"),
    path('hello/', helloWorld, name="hello")
]