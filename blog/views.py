from django.shortcuts import render

# Create your views here.
def blog(reqeust):
    return render(reqeust,'blog/blog.html')

def blog_write(request):
    return render(request,'blog/create.html')