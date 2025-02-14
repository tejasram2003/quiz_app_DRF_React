from django.shortcuts import render
from .serializers import QuestionSerializer, QuizSerializer, UserDetailSerializer, UserListSerializer
from .models import Question, Quiz
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response



# Create your views here.

class QuizViewset(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Quiz.objects.filter(creator=self.request.user.id) # This will return all quizzes created by the user
    
    def get_object(self):
        obj = super().get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied("You do not have permission to access this quiz.")
        return obj
    

class QuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(quiz__creator=self.request.user.id) # This will return all questions created by the user


    def perform_create(self, serializer):
        quiz = serializer.validated_data['quiz']
        question_number = serializer.validated_data['question_number']
        if Question.objects.filter(quiz=quiz, question_number=question_number).exists():
            return Response({"error": "A question with this number already exists in the quiz."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
    


# Authentication and User Management

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer