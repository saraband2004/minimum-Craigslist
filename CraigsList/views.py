from django.shortcuts import render, redirect
from django.http import HttpResponse
from listing.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from django.db.models import Q




def tosearch(request):
      return render(request, 'searchpage.html')


def first(request):
    return render(request, 'firstpage.html')


def post(request):
    return render(request, 'postpage.html')


def thankyou(request):
    return render(request, 'postedpage.html')


def recentlisting(request):
    junk = {
        'postxlist': Post.objects.all().order_by('-id')[:20]
        #'postlist': Post.objects.all()
    }
    return render(request, 'recentlistingpage.html', junk)


class PostListView(ListView):
    model = Post
    template_name = 'recentlistingpage.html'
    context_object_name = 'postxlist'
    ordering = ['-id']


class PostListView_2(ListView):
    model = Post
    template_name = 'searchresultpage.html'
    context_object_name = 'postxlist'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'samplepage.html'
    context_object_name = 'apost'


class PostCreateView (CreateView):
    model = Post
    template_name = 'postpage.html'
    fields = ['caption', 'texts']
    success_url = reverse_lazy('thank_you')

#def search(request):
#    junk = {
#        'postlist': Post.objects.filter(caption__contains='bmw').order_by('-id')
#    }
#    return render(request, 'searchresultpage.html', junk)

class PostSearchListView(PostListView_2):
    """
    Display a Blog List page filtered by the search query.
    """
   # query = self.request.GET.get('q')
    def get_queryset(self):
        #result = super(PostSearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        return (Post.objects.filter(caption__contains=query)|Post.objects.filter(texts__contains=query)).order_by('-id')


def search2(request):
    query = request.GET.get('q')
    junk = {
        'postxlist': (Post.objects.filter(caption__contains=query)|Post.objects.filter(texts__contains=query)).order_by('-id'),
        'pppp': {'key': query}
    }
    return render(request, 'searchresultpage.html', junk)


def search2caption(request):
    query = request.GET.get('q')
    junk = {
        'postxlist': (Post.objects.filter(caption__contains=query)).order_by('-id'),
        'pppp': {'key': query}
    }
    return render(request, 'searchresultpage.html', junk)