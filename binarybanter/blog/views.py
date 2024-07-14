from django.views import generic
from .models import Post, Subscription, QuesModel
from .forms import Postform, SubscriptionForm, addQuestionform
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
import readtime
from django.contrib import messages



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
    context = {}
    return render(request, './about.html', context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            messages.success(request, f'Successfully subscribed with {email}')
        else:
            messages.error(request, 'Subscription failed. Please enter a valid email.')
        return redirect('home')
    return redirect('home')

def quiz_category_view(request):
    context =  {}
    return render(request,'./quiz_categories.html',context)


def quiz_view(request):
    category = request.GET.get('category')
    category_dict = {'brainbenders': 1, 'brainbreach' : 2, 'circuitcore': 3, 'softwareshowdown': 4}
    if category_dict[category] == 1:
        questions=QuesModel.objects.filter(category_id_id = 1)
    if category_dict[category] == 2:
        questions=QuesModel.objects.filter(category_id_id = 2)
    if category_dict[category] == 3:
        questions=QuesModel.objects.filter(category_id_id = 3)
    if category_dict[category] == 4:
        questions=QuesModel.objects.filter(category_id_id = 4)
    
    if request.method == 'POST':
        print("printing category in post:", category)
        score=0
        wrong=0
        correct=0
        total=0
        search_query = request.POST
        db_ans = []
        user_response = []

        for items in questions:
            db_ans.append(items.ans)
        print(db_ans)
        
        for key, value in list(search_query.items())[1:-1]:
            user_response.append(value)
        print(user_response)

        for i in range(len(db_ans)):
            total+=1
            if db_ans[i] == user_response[i]:
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':format(percent, '.2f')
        }
        return render(request,'./quiz_result.html',context)
    else:
        context = {
            'questions':questions,
            'category': category
        }
        return render(request,'./quiz_template.html',context)

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'./addQuestion.html',context)
    else: 
        return redirect('home') 


def quizresults(request):
    context = {}
    return render(request, './quiz_result.html', context)