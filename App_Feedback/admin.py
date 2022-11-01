from django.contrib import admin
from .models import *


class adminFeedback(admin.ModelAdmin):
    list_display = ['user', 'feedback', 'feedback_reply', 'created_at', 'updated_at']

    class Meta:
        model = FeedBackStudent


# Register your models here.


admin.site.register(FeedBackStudent, adminFeedback)
