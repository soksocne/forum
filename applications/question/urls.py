from django.urls import path

from applications.question.views import QuestionCreateView, QuestionListView, QuestionUpdateView, QuestionDeleteView

urlpatterns = [
    path('q-create/', QuestionCreateView.as_view()),
    path('q-list/', QuestionListView.as_view()),
    path('q-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('q-delete/<int:pk>/', QuestionDeleteView.as_view()),
]