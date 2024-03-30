from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Post,Comment
from django.db.models import Count
from django.http import JsonResponse


# class PostList(generic.ListView):
def PostList(request):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    popular_post = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:2]

    paginator = Paginator(queryset, 5)  # Show 2 objects per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template_name = "index.html"
    
    # Pass the paginated queryset and pagination information to the template
    return render(
        request,
        template_name,
        {
            "page_obj": page_obj,
            "popular_post" : popular_post
        },
    )

def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    popular_post = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:2]

    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "popular_post" : popular_post

        },
    )

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1
    comment.save()

    return JsonResponse({'likes': comment.likes})