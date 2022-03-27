from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from applications.comments.models import Comments
from applications.comments.serializers import CommentsSerializer
from applications.question.permissions import IsAuthor


class CommentListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthor]


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
