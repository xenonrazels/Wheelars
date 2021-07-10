from django.shortcuts import render, get_object_or_404,get_list_or_404
from .models import Blog
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from  django.views.generic import ListView
from .forms import EmailForm,CommentForm,CreateBlogForm
from django.core.mail import send_mail
from taggit.models import Tag
# Create your views here.
#class based views goes here

# class BlogListView(ListView):
#     queryset=Blog.objects.all()
#     context_object_name='blogs'
#     paginate_by=1
#     paginate_name='blogs'
#     template_name='blog/blog.html'


#Function based views goes here
def blogs(request,tag_slug=None):
    blog_list=Blog.published.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        object_list=blog_list.filter(tag__in=[tag])

    tags=get_list_or_404(Tag)
    paginator=Paginator(blog_list,2)
    page=request.GET.get('page')
    try:
        blogs=paginator.page(page)
        #if page is not an integer,deliver the first page.
    except PageNotAnInteger:
        blogs=paginator.page(1)
        #If page is out of range deliver last page of results
    except EmptyPage:
        blogs=Paginator.page(paginator.num_pages)

    return render(request, 'blog/blog.html', {'blogs':blogs,'tags':tags,'tag':tag})

def create(request):
    form=CreateBlogForm
    return render(request,'blog/create_blog.html',{'form':form})


def blog_detail(request,year,month,day,slug):
    blog=get_object_or_404(Blog,slug=slug,publish__year=year,status='published',publish__month=month,publish__day=day)
    tags=blog.tag.all()
    comments=blog.comments.filter(active=True)
    new_comment=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.blog=blog
            new_comment.save()
            new_comment=True

    else:
        form=CommentForm()
    return render(request,'blog/blog_details.html',{'blog':blog,'form':form,'comments':comments,"new_comment":new_comment,"tags":tags})


def blog_share(request,blog_id):
    blog=get_object_or_404(Blog, pk=blog_id, status='published')
    sent=False
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            blog_url=request.build_absolute_uri(blog.get_absolute_url())
            subject=f"{cd['name']} ({cd['email']}) recommends you reading \"{blog.title}\" "
            message=f"Read \"{blog.title}\" at {blog_url}\n\n {cd['name']}\'s comments:{cd ['comments']}"
            send_mail(
                subject,message,'wheelars25@gmail.com',[cd['to'],'wheelars25@gmail.com'],fail_silently=False)
            sent=True
    else:
        form=EmailForm()
    return render(request,'blog/blog_share.html',{'blog':blog,'form':form,'sent':sent})


