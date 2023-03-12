from django.shortcuts import render, redirect
from django.contrib.auth import login

from . import forms


def signup(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = forms.CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("index")
    else:
        form = forms.CustomUserCreationForm()

    context = {"form": form, "form_title": "Crie uma nova conta", "btn_value": "Criar"}
    return render(request, "form.html", context)
