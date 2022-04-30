from django.urls import path
from . import views
app_name = "library"
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.books, name="books"),
    path('book/<str:pk>/', views.bookDetail, name="book-detail"),


]


