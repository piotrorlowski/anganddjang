from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('todolists/', views.todolist_list),
    path('todolists/<int:pk>/', views.todolist_detail),
]