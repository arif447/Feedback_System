from .views import *
from django.urls import path
app_name = 'App_Feedback'

urlpatterns = [
    path('feedback/', studentFeedback, name='studentfeedback'),
    path('replay/<id>/', ReplayFeedback, name='Replayfeedback'),
    path('feedbackshow/', feedbackshow, name='feedbackshow'),
    path('feedback_history/', Feedback_History, name='feedback_history'),

]


