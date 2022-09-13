from django.shortcuts import render
from .models import Post, Profile
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    post_obj = paginator.get_page(page_number)
    return render(request, 'home/index.html', {'post_obj': post_obj})


def postpage(request,post_id):
    user_logged = User.objects.all()
    profile_logged = Profile.objects.all()
    post = Post.objects.get(id=post_id)
    return render(request, 'home/postview.html', {
        'posts': post, 'profile_logged': profile_logged, 'user_logged': user_logged
    })


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home/createpostpage.html'
    fields = ('title', 'subtitle', 'category','content', 'image','image_font', 'references',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'home/editpostpage.html'
    fields = ('title', 'subtitle',  'category', 'content', 'image','image_font', 'references')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'home/deletepostpage.html'
    success_url = reverse_lazy('home')


def searchquery(request):
    query = request.GET.get('query')

    if query == "":
        return render(request, 'home/search.html')

    post_obj = Post.objects.filter(
        Q(title__icontains=query) | Q(subtitle__icontains=query)
         )
    context = {'post_obj':post_obj}

    return render(request, 'home/search.html', context)


