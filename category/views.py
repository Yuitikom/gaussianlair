from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from home.models import Post, Category
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def category_list(request):
    category_list = Category.objects.all()
    context = {
        'category_list':category_list
    }

    return context


def categorypage(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 4)
    page_number = request.GET.get('page', 1)
    cat_obj = paginator.get_page(page_number)
    return render(request, 'category/categoriespage.html', {'cat_obj':cat_obj})


class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category/createcategorypage.html'
    fields = ('name', 'image')
    success_url = reverse_lazy('categories')


class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'category/editcategorypage.html'
    fields = ('name','image')
    success_url = reverse_lazy('categories')


class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/deletecategorypage.html'
    success_url = reverse_lazy('categories')


def categoryviewpage(request, category_name):
    categoryfilter = Category.objects.get(name=category_name)
    postscategory = Post.objects.filter(category__name=category_name)
    paginator = Paginator(postscategory, 4)
    page_number = request.GET.get('page', 1)
    cat_obj = paginator.get_page(page_number)
    return render(request, 'category/categorypage.html', {'category_name':categoryfilter,'cat_obj':cat_obj})