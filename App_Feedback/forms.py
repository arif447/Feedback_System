from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import FeedBackStudent


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class feedbackform(forms.ModelForm):
    class Meta:
        model = FeedBackStudent
        fields = ['feedback']


class replayFeedback(forms.ModelForm):
    class Meta:
        model = FeedBackStudent
        fields = ['feedback_reply']

