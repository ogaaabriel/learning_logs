from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    path("topicos_publicos/", views.public_topics, name="public_topics"),
    path("topicos_publicos/<int:topic_id>/", views.public_topic, name="public_topic"),
    path("meus_topicos/", views.topics, name="topics"),
    path("meus_topicos/<int:topic_id>/", views.topic, name="topic"),
]
