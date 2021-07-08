from django.urls import path
from django.contrib.auth import views as views_
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views_.LoginView.as_view(template_name='auth_/login.html'), name='login'),
    path('logout/', views_.LogoutView.as_view(), name='logout'),
    path('change_password/', views_.PasswordChangeView.as_view(template_name='auth_/change.html'),
         name='change_password'),
    path('password_change_done/', views_.PasswordChangeDoneView.as_view(template_name='auth_/changed.html'), name='password_change_done'),

    path('reset_password/', views_.PasswordResetView.as_view(template_name='auth_/reset.html'), name='reset_password'),
    path('password_reset_confirm/<uidb64>/<token>/',
         views_.PasswordResetConfirmView.as_view(template_name='auth_/login.html'), name='password_reset_confirm'),
    path('password_reset_complete/', RedirectView.as_view(pattern_name='main_page'), name='password_reset_complete'),
    path('password_reset_done/', views_.PasswordResetDoneView.as_view(template_name='auth_/reset_sent.html'),
         name='password_reset_done'),
]
