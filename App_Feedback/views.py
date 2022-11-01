from django.shortcuts import render,  HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import FeedBackStudent
from .forms import feedbackform,  replayFeedback

# Create your views here.


@login_required
def studentFeedback(request):
    form =feedbackform()
    if request.method == 'POST':
        form =feedbackform(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Feedback:feedback_history'))
    return render(request, 'feedback/feedback.html', context={'form': form})


@login_required
def ReplayFeedback(request, id):
    replay_feedback = FeedBackStudent.objects.get(id=id)
    form = replayFeedback(instance=replay_feedback)
    if request.method == 'POST':
        form = replayFeedback(request.POST, instance=replay_feedback)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Feedback:feedbackshow'))

    return render(request, 'feedback/replayfeedback.html', context={'form': form})

@login_required
def feedbackshow(request):
    feedback = FeedBackStudent.objects.all()
    diction = {'feedback': feedback}
    return render(request, 'feedback/feedbackshow.html', context=diction)


@login_required
def Feedback_History(request):
    student_feedback = FeedBackStudent.objects.filter(user=request.user)
    diction = {'student_feedback ': student_feedback}
    return render(request, 'feedback/feedbackhistory.html', context=diction)

