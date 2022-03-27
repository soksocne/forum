from django.urls import path
from . import views


urlpatterns = [
    path('c-list/', views.CommentListView.as_view()),
    path('c-create/', views.CommentCreateView.as_view()),
    path('c-update/<int:pk>', views.CommentUpdateView.as_view()),
    path('c-delete/<int:pk>', views.CommentDeleteView.as_view()),
]
