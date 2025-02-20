from django.urls import path
from .views import QuizViewset, UserListCreateView, UserDetailView, QuestionViewset, SubmissionViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('quizzes/', QuizViewset.as_view({'get': 'list', 'post': 'create'}), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='quiz-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quizzes/<int:quiz_id>/questions/', QuestionViewset.as_view({'get': 'list', 'post': 'create'}), name='quiz-questions'),
    path('quizzes/<int:quiz_id>/questions/<int:pk>/', QuestionViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='question-detail'),
    path('quizzes/<int:quiz_id>/submissions/', SubmissionViewset.as_view({'get': 'list', 'post': 'create'}), name='quiz-submissions'),
]

