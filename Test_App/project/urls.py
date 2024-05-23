from django.urls import path
from career_test import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Здесь определите маршруты для вашего приложения
    path('', views.index, name='index'),
    path('answer/<int:answer_id>/', views.answer_detail, name='answer_detail'),
    path('submit/', views.submit_answers, name='submit_answers'),
    path('users/', views.user_list, name='user_list'),
]
