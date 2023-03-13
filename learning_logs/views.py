from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from . import models, forms, helpers


def public_topics(request):
    topics = models.Topic.objects.filter(public=True)

    search = request.GET.get("q", "")
    if search:
        topics = helpers.search_topics(search, topics)

    topics_page = helpers.paginate(request, topics, 1)
    context = {"topics": topics_page, "public": True, "search": search}
    return render(request, "learning_logs/topics.html", context)


def public_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, public=True, id=topic_id)
    entries = topic.entries.all()
    entries_page = helpers.paginate(request, entries, 1)
    context = {"topic": topic, "entries": entries_page, "public": True}
    return render(request, "learning_logs/topic.html", context)


@login_required
def topics(request):
    topics = models.Topic.objects.filter(owner=request.user)

    search = request.GET.get("q", "")
    if search:
        topics = helpers.search_topics(search, topics)

    topics_page = helpers.paginate(request, topics, 1)
    context = {"topics": topics_page, "search": search}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    topic = get_object_or_404(models.Topic, owner=request.user, id=topic_id)
    entries = topic.entries.all()
    entries_page = helpers.paginate(request, entries, 1)
    context = {"topic": topic, "entries": entries_page}
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


@login_required
def copy_topic(request, topic_id):
    topic = get_object_or_404(models.Topic, public=True, id=topic_id)

    if request.method != "POST":
        raise Http404

    title_exists = models.Topic.objects.filter(
        title__iexact=topic.title, owner=request.user
    ).exists()

    if title_exists:
        messages.error(request, "Você já possui um tópico com esse título!")
    else:
        topic.pk = None
        topic.owner = request.user
        topic.public = False
        topic.save()

        for entry in models.Entry.objects.filter(topic__id=topic_id):
            entry.pk = None
            entry.topic = topic
            entry.save()

        messages.success(request, "Tópico copiado com sucesso!")

    return redirect("learning_logs:public_topic", topic_id=topic_id)


@login_required
def create_entry(request, topic_id):
    topic = get_object_or_404(models.Topic, owner=request.user, id=topic_id)

    if request.method == "POST":
        form = forms.EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            messages.success(request, "Registro adicionado com sucesso!")
            return redirect("learning_logs:topic", topic_id=topic_id)
    else:
        form = forms.EntryForm()

    context = {
        "form": form,
        "form_title": "Adicione um novo registro",
        "btn_value": "Adicionar",
    }
    return render(request, "form.html", context)


@login_required
def update_entry(request, entry_id):
    entry = get_object_or_404(models.Entry, topic__owner=request.user, id=entry_id)

    if request.method == "POST":
        form = forms.EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro editado com sucesso!")
            return redirect("learning_logs:topic", topic_id=entry.topic.id)
    else:
        form = forms.EntryForm(instance=entry)

    context = {
        "form": form,
        "form_title": "Editar registro",
        "btn_value": "Salvar",
    }
    return render(request, "form.html", context)


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(models.Entry, topic__owner=request.user, id=entry_id)
    topic = entry.topic

    if request.method == "POST":
        entry.delete()
        messages.success(request, "Registro excluído com sucesso!")
        return redirect("learning_logs:topic", topic_id=topic.id)
    else:
        raise Http404
