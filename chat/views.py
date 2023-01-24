from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from taggit.models import Tag, TaggedItem

from .forms import NewCommentForm
from .models import Post, Comment


class Home(generic.TemplateView):
    template_name = 'index.html'


@receiver(post_delete, sender=TaggedItem)
def delete_unused_tags(sender, instance, **kwargs):
    n_tagged = TaggedItem.objects.filter(tag_id=instance.tag_id).count()
    if n_tagged == 0:
        instance.tag.delete()

def search(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | \
                                    Q(content__icontains=search_post))
    else:
        posts = Post.objects.order_by('-updated_on')
    return render(request, 'chat.html', {'posts': posts})


def tagged(request, slug):
    tags = Tag.objects.order_by('-name')
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)

    return render(request, 'chat.html', {'tag': tag, 'posts': posts, 'tags': tags})


def postList(request):
    tags = Tag.objects.order_by('-name')
    posts = Post.objects.order_by('-updated_on')
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
        'tags': tags,
        'posts': posts,
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
