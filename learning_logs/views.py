from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import models


def public_topics(request):
    topics = models.Topic.objects.filter(public=True)
    context = {"topics": topics, "public": True}
    return render(request, "learning_logs/topics.html", context)


def public_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, public=True, id=topic_id)
    entries = topic.entries.all()
    context = {"topic": topic, "entries": entries, "public": True}
    return render(request, "learning_logs/topic.html", context)


@login_required
def topics(request):
    topics = models.Topic.objects.filter(owner=request.user)
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    topic = get_object_or_404(models.Topic, owner=request.user, id=topic_id)
    entries = topic.entries.all()
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
