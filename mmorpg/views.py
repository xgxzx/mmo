from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
from .forms import UserForm, ProfileForm, CategoryForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post


def category_list_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'mmorpg/category/category_list.html', context)

@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'mmorpg/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=profile)
    context = {'profile': profile, 'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'mmorpg/profile.html', context)


# class PostList(ListView):
#     model = Post
#     template_name = 'mmorpg/post_list.html'
#     context_object_name = 'post'
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'mmorpg/post_list.html', context)
