from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User, Role


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def profile_redactor(request, id):
    user = User.objects.get(id=id)
    form = UserForm(instance=user)
    if request.method == "POST":
        # form = UserForm(request.POST, instance=request.user)
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user.avatar = form.cleaned_data.get("avatar")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.about = request.POST.get("about")
            user.facebook_id = request.POST.get("facebook_id")
            user.twitter_id = request.POST.get("twitter_id")
            user.birth_date = request.POST.get("birth_date")
            user.save()
            return redirect(f"http://127.0.0.1:8000/profile/dge{id}du/")
        else:
            form = UserForm()
    return render(
        request,
        "intranet/user/profile_editor.html",
        {"form": form, "avatar": user.avatar},
    )


def organization_page(request):
    roles = Role.objects.all()
    return render(
        request,
        "intranet/organization.html",
        {"roles": roles},
    )
