from django.urls import path
from . import views
app_name = "library"
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.userDashboard, name="books"),
    path('book/<str:pk>/', views.bookDetail, name="book-detail"),

    path('libadmin/book/<str:pk>/', views.adminBookDetail, name="admin-book-detail"),
    path('libadmin/manage/', views.manageBooks, name="manage-books"),
    path('libadmin/add/book/', views.addBook, name="add-book"),
    path('libadmin/add/author/', views.addAuthor, name="add-author"),
    path('libadmin/add/publisher/', views.addPublisher, name="add-publisher"),
    path('libadmin/edit/<str:pk>/', views.editBookDetail, name="edit-book-detail"),
    path('libadmin/delete/<str:pk>/', views.deleteBook, name="delete-book"),



]


