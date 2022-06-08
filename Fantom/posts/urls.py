from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('detail/<int:pk>/<slug:slug>', PostDetail.as_view(), name="detail"),
    path('category/<int:pk>/<slug:slug>', CategoryDetails.as_view(), name="category_detail"),
]
