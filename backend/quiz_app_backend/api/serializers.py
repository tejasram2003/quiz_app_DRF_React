from rest_framework import serializers
from .models import Question, Quiz


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from typing import Dict, Any

# sending mails and generating tokens
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from .utils import generate_token
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from django.db import transaction
from rest_framework.exceptions import ValidationError



class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Make id optional for new questions

    class Meta:
        model = Question
        fields = ['id', 'question', 'options', 'correct_option']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    creator = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'creator', 'questions', 'created_at', 'updated_at', 'deadline']
    

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')


        user = self.context['request'].user

        quiz = Quiz.objects.create(creator=user, **validated_data)
        
        # Bulk create questions
        Question.objects.bulk_create([
            Question(quiz=quiz, **question_data)
            for question_data in questions_data
        ])
        
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions')
        
        # Update quiz fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        with transaction.atomic():
            # Delete existing questions
            instance.questions.all().delete()
            
            # Bulk create new questions
            Question.objects.bulk_create([
                Question(quiz=instance, **question_data)
                for question_data in questions_data
            ])
        
        return instance

# Serializers for User creation and authentication

class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'isAdmin', 'token', 'name', 'email']

    def get_name(self, obj):
        name = f"{obj.first_name} {obj.last_name}".strip()
        return name if name else obj.username
    
    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     default_error_messages = {
#         'no_active_account': 'Invalid credentials.',
#     }

#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['username'] = user.username
#         return token
    
#     def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:

#         data = super().validate(attrs)
#         if self.user is None:
#             raise serializers.ValidationError("No account with the provided credentials, please sign up instead.")
#         serializer = UserDetailSerializer(self.user).data
#         for k, v in serializer.items():
#             data[k] = v
#         return data


class UserListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'is_staff': {'read_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_active': {'read_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            is_active=False,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()

        # email_subject = 'Activate your account'
        # message = render_to_string(
        #     "activate.html",
        #     {
        #         'user': user,
        #         'domain': "127.0.0.1:8000",
        #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #         'token': generate_token.make_token(user)
        #     }
        # )

        # email_message = EmailMessage(
        #     subject=email_subject,
        #     body=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     to=[user.email]
        # )
        # email_message.send()

        return user