import io, csv
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Paste
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django import  forms
from .forms import UploadFileForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.admin.widgets import AdminDateWidget


#from django.contrib.admin import widgets

# Create your views here.
#romel was here
from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(date_expired__gt=datetime.now())
    template_name= 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("search", " ")
        if query:
            return Post.objects.filter((Q(title__icontains=query)| Q(content__icontains=query)| Q(author__username=query)) & Q(date_expired__gt=datetime.now())).order_by('-date_posted')

class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(Q(author=user)).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #date_expired = forms.DateTimeField(widget=forms.SplitDateTimeWidget())

    fields = ['title', 'content', 'date_expired', 'private']
    #widgets = {'date_expired': forms.DateTimeField()}
    from_date = forms.DateField(widget=AdminDateWidget())
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'date_expired', 'private']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def PostDownload(request,pk,**kwargs):
    model = Post
    title = Post.objects.only('title').get(id=pk).title + ".txt"
    content = Post.objects.only('content').get(id=pk).content
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition']='attachment; filename="%s"' %  str(title)
    return response


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)

class PasteCreateView(LoginRequiredMixin, CreateView):
    model = Paste
    fields = ['title', 'content', 'date_expired', 'private']

  #  date_expired = forms.DateField(forms.widgets.SelectDateWidget())

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newpost= Post()
            newpost.title = request.POST.get("title", "")
            newpost.content = request.FILES['file'].read()
            newpost.date_posted = datetime.now()
            newpost.date_expired= request.POST.get("date_expired","")
            newpost.author = request.user
            #print(request.FILES['file'].size)
            #print(newpost.title)
            #print(newpost.content)
            #print(newpost.date_posted)
            #print(newpost.date_expired)
            #print(newpost.author)
            newpost.save()
            messages.success(request, "Post from file created!")
            return redirect('/')
        else:
            form = UploadFileForm()
            messages.error(request, "File is too big, or invalid. It can only be a .txt!")
    else:
        form = UploadFileForm()
    return render(request, 'blog/uploadfile.html', {'form': form})
