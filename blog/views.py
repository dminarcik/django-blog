from blog.forms import CommentForm, PostModelForm
from blog.models import Comment, Post
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CreatePost(CreateView):
    model = Post
    form_class = PostModelForm
    template_name = "blog/post.html"
    success_url = reverse_lazy("blog_index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        print(obj)
        return super().form_valid(form)

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "form": form}

    return render(request, "blog/detail.html", context)
