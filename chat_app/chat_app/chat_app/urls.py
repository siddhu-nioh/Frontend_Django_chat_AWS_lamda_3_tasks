from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),  # Registration view
    path('chat/', views.default_chat_view, name='default_chat'),  # Default chat view
    path('chat/<int:receiver_id>/', views.chat_view, name='chat'),  # Chat with a specific user
    path('accounts/profile/', views.profile_view, name='profile'),  # Profile view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]