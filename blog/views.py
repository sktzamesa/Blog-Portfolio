from django.shortcuts import render,get_object_or_404
from .models import Post,Portfolio,About
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from django.views.decorators.http import require_POST,require_GET
from .forms import EmailPostForms,CommentForm,SearchForm,ContactForm
from django.views.generic import ListView
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank
    )
from django.contrib.postgres.operations import TrigramExtension
# Create your views here.
#class PostListView(ListView):
#    queryset = Post.published.all()
#    context_object_name = 'posts'
#    paginate_by = 3
#    template_name = 'blog/post/list.html'
@require_GET
def post_list(request,tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(
            Tag,
            slug=tag_slug
        )
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list,per_page=6)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(
        request,
        'blog/post/list.html',
    {
        'posts':posts,
        'tag':tag,
    }
    )

def post_detail(request,year,month,day,post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(
        request,
        'blog/post/detail.html',
        {
            'post':post,
            'comments':comments,
            'form':form,
            'similar_posts':similar_posts
         }
        )

def post_share(request,post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )
    sent = False

    if request.method == 'POST':
        form = EmailPostForms(data = request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = (
                f"{cd['name']} ({cd['email']})"
                f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comment']}"
            )
            send_mail(
                subject = subject,
                message = message,
                from_email = None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForms()

    return render(
        request,
        'blog/post/share.html',
        {
            'post':post,
            'form':form,
            'sent':sent,
        }
    )

@require_POST
def post_comment(request,post_id):
    post = get_object_or_404(
        Post,
        id = post_id,
        status=Post.Status.PUBLISHED
    )

    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        'blog/post/comment.html',
        {
            'post':post,
            'form':form,
            'comment':comment,
        }
    )


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_query = SearchQuery(query, config='spanish')
            search_vector=(SearchVector('title',config='spanish',weight = 'A') +
                                        SearchVector('body',config = 'spanish',weight='B'))
            results = (
                Post.published.annotate(search=search_vector,rank=SearchRank(search_vector,search_query)
                                        ).filter(search=search_query).order_by('-rank')
            )
    return render(
        request,
        'blog/post/search.html',
        {
            'form':form,
            'query':query,
            'results':results
        }
    )
def portfolio(request):
    portfolio = Portfolio.objects.first()
    return render(
        request,
        'blog/post/portfolio.html',
        {'portfolio':portfolio}
    )

def about(request):
    about = About.objects.first()
    return render(
        request,
        'blog/post/about.html',
        {
            'about':about
        }
    )

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = (
                f"{cd['name']} ({cd['email']})"
                f"Someone is interested to you"
            )
            message = (
                     f"The message sent to you is from {cd['name']}. "
                     f"The phone number is {cd['phone']}. "
                     f"Message: {cd['message']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=['qzamesa@gmail.com']
            )
            sent = True
    else:
        form = ContactForm()

    return render(
        request,
        'blog/post/contact.html',
        {
            'form':form,
            'sent':sent

        }

    )














