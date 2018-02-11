from django.shortcuts import render, redirect
from blogging.models import Author, Post
from django.views import generic
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

class Index(generic.ListView):
    template_name = "blogging/index.html"
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-date_created')

class PostView(generic.DetailView):
    template_name = "blogging/post_detail.html"
    model = Post

#class SendView(LoginRequiredMixin, generic.TemplateView):
#    template_name = "blogging/post_post.html"
#    model = Post
#    form = PostForm()
#class TestView(generic.TemplateView):
#    template_name = "blogging/test.html"
#    model = Post

def SendView(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
        else:
            form = PostForm()
    return render(request, 'blogging/post_post.html', {'form':form})


    