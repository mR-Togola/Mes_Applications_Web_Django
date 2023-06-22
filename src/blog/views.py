from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from blog.models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    fields = ['title', 'content','published',]
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset =  super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "blog/blogpost_create.html"
    fields = ['title', 'content','published',]


class BloPostUpdate(UpdateView):
    model = BlogPost
    template_name = "blog/blogpost_edit.html"
    fields = ['title', 'content','published',]
        
 

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

class BlosPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")



