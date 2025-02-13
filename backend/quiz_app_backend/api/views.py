from django.shortcuts import render
from .serializers import QuestionSerializer, QuizSerializer
from .models import Question, Quiz
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class QuizList(ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(creator=self.request.user)

class QuizDetail(RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer