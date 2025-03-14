from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views import category_list, category_create, category_update, category_delete

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('categories/', category_list, name='category-list'),
    path('categories/new/', category_create, name='category-create'),
    path('categories/<int:pk>/edit/', category_update, name='category-update'),
    path('categories/<int:pk>/delete/', category_delete, name='category-delete'),
]

