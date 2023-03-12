from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    path("topicos_publicos/", views.public_topics, name="public_topics"),
    path("topicos_publicos/<int:topic_id>/", views.public_topic, name="public_topic"),
    path("meus_topicos/", views.topics, name="topics"),
    path("meus_topicos/<int:topic_id>/", views.topic, name="topic"),
    path("adicionar_topico/", views.create_topic, name="create_topic"),
    path("editar_topico/<int:topic_id>/", views.update_topic, name="update_topic"),
    path("excluir_topico/<int:topic_id>/", views.delete_topic, name="delete_topic"),
    path("adicionar_registro/<int:topic_id>/", views.create_entry, name="create_entry"),
    path("editar_registro/<int:entry_id>/", views.update_entry, name="update_entry"),
    path("excluir_registro/<int:entry_id>/", views.delete_entry, name="delete_entry"),
]
