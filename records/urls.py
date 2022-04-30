from django.urls import path
from . import views
app_name = "records"

urlpatterns = [
    path('confirm/<str:pk>/', views.confirmRequest, name="confirm"),
]


