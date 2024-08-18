from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'author', 'preview_img')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'author', 'preview_img')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostArchiveListView(ListView):
    model = Post
    template_name = 'blog/post_archive_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=False)
        return queryset

    def get_success_url(self):
        return reverse_lazy('blog:archive')

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.is_published:
            self.object.views_count += 1
        self.object.save()
        return self.object

class PostDeleteView(DeleteView):
    model = Post
    if model.is_published:
        success_url = reverse_lazy('blog:list')
    else:
        success_url = reverse_lazy('blog:archive')


def toggle_is_published(request, pk):
    post_item = get_object_or_404(Post, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
        post_item.save()

        return redirect(reverse_lazy('blog:list'))
    else:
        post_item.is_published = True
        post_item.save()

        return redirect(reverse_lazy('blog:archive'))

