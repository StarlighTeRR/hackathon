from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.http import JsonResponse
import json

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return JsonResponse({'success': True, 'message': 'User registered successfully'})
#         else:
#             return JsonResponse({'success': False, 'message': 'Invalid form data', 'errors': form.errors})
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method'})

# def login_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         login = data.get('login')
#         password = data.get('password')

#         # Здесь вы можете добавить проверку логина и пароля
#         if login == 'test@example.com' and password == 'password123':
#             return JsonResponse({'message': 'Login successful'}, status=200)
#         else:
#             return JsonResponse({'message': 'Invalid credentials'}, status=401)
#     return JsonResponse({'message': 'Method not allowed'}, status=405)


def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Logged in successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
