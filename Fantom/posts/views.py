from re import template
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class IndexView(ListView):
    template_name = "posts/index.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


class CategoryDetails(ListView):
    model = Post
    template_name = 'categories/categories_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoryDetails, self).get_context_data(**kwargs)
        return context
