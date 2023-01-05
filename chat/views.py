from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import NewCommentForm
from .models import Post, Comment
from django import forms


class Home(generic.TemplateView):
    template_name = 'index.html'


def PostList(request):
    queryset = Post.objects.order_by('-updated_on')
    if request.method == 'POST':
        pk = request.POST.get('post')
        post = Post.objects.get(id=pk)
        comment_form = NewCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.posts = post
            comment_form.save()
            return redirect('posts')
    else:
        comment_form = NewCommentForm()
    context = {
        'posts': queryset,
        'form': comment_form
    }
    return render(request, 'chat.html', context)


class NewPost(generic.CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'
    success_url = ''

def delete_post(request, pk=None):
    post_to_delete = Post.objects.get(id=pk)
    post_to_delete.delete()
    return HttpResponseRedirect('../posts')


def delete_comment(request, pk):
    Comment.objects.get(pk=pk).delete()
    return HttpResponseRedirect('../posts')


class NewComment(generic.CreateView):
    model = Comment
    form_class = NewCommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.id_post = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
