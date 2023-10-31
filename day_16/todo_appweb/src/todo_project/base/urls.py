from django.urls import path
from .views import TodoList, TaskDetail, CreateTask, EditTask, DeleteTask, LogIn, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TodoList.as_view(), name='todo'),
    path('login/', LogIn.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')
]
