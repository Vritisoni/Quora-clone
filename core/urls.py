from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('questions/', views.question_list, name='question_list'),

    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),

]
