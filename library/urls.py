from django.urls import path
from . import views
app_name = "library"
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.userDashboard, name="books"),
    path('book/<str:pk>/', views.bookDetail, name="book-detail"),

    path('manage/', views.manageBooks, name="manage-books"),
    path('add/book/', views.addBook, name="add-book"),
    path('add/author/', views.addAuthor, name="add-author"),
    path('add/publisher/', views.addPublisher, name="add-publisher"),
    path('edit/<str:pk>/', views.editBookDetail, name="edit-book-detail"),
    path('delete/<str:pk>/', views.deleteBook, name="delete-book"),



]


