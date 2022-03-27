from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.question.views import QuestionCreateView, QuestionListView, QuestionUpdateView, QuestionDeleteView, \
    QuestionViewSet

router = DefaultRouter()
router.register('', QuestionViewSet)


urlpatterns = [
    path('q-create/', QuestionCreateView.as_view()),
    path('q-list/', QuestionListView.as_view()),
    path('q-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('q-delete/<int:pk>/', QuestionDeleteView.as_view()),
]
urlpatterns.extend(router.urls)
