
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_view, name = "logout_page"),
    path('login/', views.login_view, name="login_page"),
    path('register/', views.register_view, name="register_page"),
    path('delete-transaction/<id>', views.delete_transaction, name="delete_transaction")
]