from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.profile_image:
                user.profile_image = "profile_images/no-avatar.png"
            user.save()
            auth_login(request, user)
            return redirect("articles:index")
        else:
            print("error")
            print(form.error_messages)
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        else:
            messages.warning(request, "아이디 또는 비밀번호가 틀렸습니다.")
        return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")


@login_required
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    followers_number = user.followers.count()
    followings_number = user.followings.count()
    context = {
        "user": user,
        "followers_number": followers_number,
        "followings_number": followings_number,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def profile_update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.profile_image:
                user.profile_image = "profile_images/no-avatar.png"
            user.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def password_update(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:detail", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_POST
def delete(request):
    try:
        request.user.delete()
        auth_logout(request)
        messages.success(request, "탈퇴하였습니다.")
    except:
        messages.error(request, "error")
        return render(request, "reviews:index")
    return redirect("reviews:index")


@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), id=pk)
    if user != request.user:
        if request.user in user.followers.all():
            user.followers.remove(request.user)
            is_followed = False
        else:
            user.followers.add(request.user)
            is_followed = True
        context = {
            "is_followed": is_followed,
            "followings_count": user.followings.count(),
            "followers_count": user.followers.count(),
        }
        return JsonResponse(context)
    else:
        messages.error(request, "자신을 팔로우할 수 없습니다")
