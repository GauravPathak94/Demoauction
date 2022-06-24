from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.RegistrationView.as_view(), name='reg_url'),
    path('log/', views.LoginView.as_view(), name='login_url'),
    path('out/', views.LogoutView.as_view(),name='logout'),
    path('otp', views.OTPView.as_view(), name='otp_url'),
    path('activate/<uidb64>/<token>/',views.ActivateAccountView.as_view(), name='activate'),
    path('', views.HomeView.as_view(), name='home'),
    path('sv/<int:id>/', views.showUserView, name='show_url'),
    path('uv/<int:id>/', views.updateProfileView, name='update_url'),
    path('dl/<int:id>/', views.deleteProfileView, name='delete_url')
    ]