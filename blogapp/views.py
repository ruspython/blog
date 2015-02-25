from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-timestamp')
    template_name = 'blogapp/list.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # context['tags']
        return context

    # TODO: tags


class PostByTagListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-timestamp')
    template_name = 'blogapp/list.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.filter(tags__name__iexact=self.kwargs['tag_name'])


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/detail.html'
    context_object_name = 'post'

    def dispatch(self, request, *args, **kwargs):
        return super(PostDetailView, self).dispatch(request, *args, **kwargs)

        # TODO: tags