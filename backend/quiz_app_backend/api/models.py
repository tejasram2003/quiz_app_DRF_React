from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']

class Quiz(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):

        if self.deadline:
            if self.deadline < self.created_at:
                raise ValueError("Deadline cannot be before the creation date")
            
        return super().save(force_insert, force_update, using, update_fields)
    
class Question(models.Model):
    OPTION_CHOICES = [
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    options = models.JSONField()
    correct_option = models.PositiveSmallIntegerField(choices=OPTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['id']

    

class Submissions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    score = models.PositiveSmallIntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
    
    class Meta:
        ordering = ['-submitted_at']