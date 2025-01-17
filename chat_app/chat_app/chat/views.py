from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .models import ChatMessage

# Use Django's built-in login view
login_view = auth_views.LoginView.as_view(template_name='login.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Default Chat View
@login_required
def default_chat_view(request):
    # Redirect to the chat page of the first user in the list
    first_user = User.objects.exclude(id=request.user.id).first()
    if first_user:
        return redirect('chat', receiver_id=first_user.id)
    else:
        return render(request, 'no_users.html')  # Handle case where no users exist

# Profile View
@login_required
def profile_view(request):
    return render(request, 'profile.html')

# Chat View@login_required
def chat_view(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    users = User.objects.exclude(id=request.user.id)  # Ensure this line is correct
    messages = ChatMessage.objects.filter(sender=request.user, receiver=receiver) | ChatMessage.objects.filter(sender=receiver, receiver=request.user)
    return render(request, 'chat.html', {
        'users': users,
        'messages': messages.order_by('timestamp'),
        'receiver': receiver,
        'receiver_username': receiver.username
    })