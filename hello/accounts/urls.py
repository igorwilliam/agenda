from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('novo-usuario/', views.addUser, name='addUser'),
    path('login-usuario/', views.loginUser, name='loginUser'),
    path('logout-usuario/', views.logoutUser, name='logoutUser'),
    path('alterar-senha/', views.changePassword, name='changePassword'),
]
