from django.views import generic
from .models import Post
from .forms import Postform
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
import readtime



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'home.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        model = Post
        context = super().get_context_data(**kwargs)
        for item in model.objects.filter(slug=self.kwargs.get('slug')):
            time = str(readtime.of_markdown(item.content))
            print(time)
        context['extra_key'] = time
        return context

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