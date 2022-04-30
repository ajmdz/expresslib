from django.urls import path
from . import views
app_name = "records"

urlpatterns = [
    path('confirm/<str:pk>/', views.confirmRequest, name="confirm"),
    path('requests/', views.fetchRequests, name="borrow-requests"),
    path('approve/<int:pk>/', views.approveRequest, name="approve-request"),
    path('decline/<int:pk>/', views.declineRequest, name="decline-request"),
]


