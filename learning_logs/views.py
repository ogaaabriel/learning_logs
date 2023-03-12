from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from . import models, forms


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


@login_required
def create_topic(request):
    if request.method == "POST":
        form = forms.TopicForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            messages.success(request, "Tópico adicionado com sucesso!")
            return redirect("learning_logs:topic", topic_id=new_topic.id)
    else:
        form = forms.TopicForm()

    context = {
        "form": form,
        "form_title": "Adicione um novo tópico",
        "btn_value": "Adicionar",
    }
    return render(request, "form.html", context)


@login_required
def update_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, owner=request.user, id=topic_id)

    if request.method == "POST":
        form = forms.TopicForm(
            instance=topic, data=request.POST, user=request.user, topic_id=topic.id
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Tópico editado com sucesso!")
            return redirect("learning_logs:topic", topic_id=topic_id)
    else:
        form = forms.TopicForm(instance=topic)

    context = {
        "form": form,
        "form_title": "Editar tópico",
        "btn_value": "Salvar",
    }
    return render(request, "form.html", context)


@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, owner=request.user, id=topic_id)

    if request.method == "POST":
        topic.delete()
        messages.success(request, "Tópico excluído com sucesso!")
        return redirect("learning_logs:topics")
    else:
        raise Http404
