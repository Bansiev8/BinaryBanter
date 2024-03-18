from django.views import generic
from .models import Post
from .forms import Postform
from django.urls import reverse_lazy
from django.shortcuts import render, redirect



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'home.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class Addblog(generic.CreateView):
    model=Post
    form_class= Postform
    template_name='add_blog.html'
    # fields = '__all__'

class Updateblog(generic.UpdateView):
    model = Post
    template_name = 'update_blog.html'
    fields = '__all__'


class Deleteblog(generic.DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')


def about(request):
    # blog_list = Post.objects.all().reverse()
    context = {}
    return render(request, './about.html', context)