from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.


class Account(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.user.username} ({self.role})"


    class Meta:
        ordering = ['id']

from django.core.exceptions import ValidationError

class Quiz(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.deadline and self.deadline < self.created_at:
            raise ValidationError("Deadline cannot be before the creation date.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        super().save(*args, **kwargs)

    
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

    

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    score = models.FloatField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"
    
    class Meta:
        ordering = ['-submitted_at']


class UserAnswer(models.Model):
    submission = models.ForeignKey("Submission", on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.PositiveSmallIntegerField(null=True, blank=True)  # Stores 1, 2, 3, or 4
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.selected_option is not None:  # If user answered
            self.is_correct = (self.selected_option == self.question.correct_option)
        super().save(*args, **kwargs)

