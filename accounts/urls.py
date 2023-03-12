from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "entrar/",
        LoginView.as_view(
            template_name="form.html",
            redirect_authenticated_user=True,
            extra_context={"form_title": "Acesse sua conta", "btn_value": "Entrar"},
        ),
        name="login",
    ),
    path("sair/", LogoutView.as_view(), name="logout"),
    path("criar_conta/", views.signup, name="signup"),
]
