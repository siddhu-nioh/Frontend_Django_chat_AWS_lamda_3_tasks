from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration view
    path('chat/', views.default_chat_view, name='default_chat'),  # Default chat view
    path('chat/<int:receiver_id>/', views.chat_view, name='chat'),  # Chat with a specific user
    path('accounts/profile/', views.profile_view, name='profile'),  # Profile view
]