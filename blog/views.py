from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .models import words
# Create your views here.

categories = ['Current Affairs', 'Business', 'Technology', 'Entertainment', 'Sports', 'Science','Health','Uncategorized']


def blog_list(request,tags):
    blogs = get_list_or_404(words,tags=tags)
    popular = words.objects.filter(popular=True)
    books = words.objects.all()
    unique = []
    uniquetags = []
    for book in books:
        if book.tags in uniquetags:
            pass
        else:
            unique.append(book)
            uniquetags.append(book.tags)
    return render(request,'blog_list.html',{'blogs':blogs,'popular':popular,'categories':categories,'unique':unique})

def blog_categorylist(request,category):
    popular = words.objects.filter(popular=True)
    blogs = get_list_or_404(words,category=category)
    books = words.objects.all()
    unique = []
    uniquetags = []
    for book in books:
        if book.tags in uniquetags:
            pass
        else:
            unique.append(book)
            uniquetags.append(book.tags)
    return render(request,'blog_list.html',{'blogs':blogs,'popular':popular,'categories':categories,'unique':unique})

def post_detail(request,pk):
    post = get_object_or_404(words,pk=pk)
    blogs = words.objects.all()
    popular = words.objects.filter(popular=True)
    books = words.objects.all()
    unique = []
    uniquetags = []
    for book in books:
        if book.tags in uniquetags:
            pass
        else:
            unique.append(book)
            uniquetags.append(book.tags)
    return render(request, 'post_detail.html',{'post':post,'blogs':blogs,'popular':popular,'unique':unique,'categories':categories})

def write(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            blog1 = words()
            blog1.title = request.POST['title']
            blog1.tags = request.POST['tags']
            blog1.body = request.POST['body']
            blog1.author = request.user.first_name +" " + request.user.last_name
            blog1.category = request.POST['category']
            blog1.save()
            return redirect('/')
        
    elif request.user.is_authenticated:
        return render(request,"write.html")
    else:
        return redirect('login')

def index(request):
    popular = words.objects.filter(popular=True)
    blogs = words.objects.all()
    books = words.objects.all()
    unique = []
    uniquetags = []
    for book in books:
        if book.tags in uniquetags:
            pass
        else:
            unique.append(book)
            uniquetags.append(book.tags)
    return render(request,"index.html",{'blogs':blogs,'popular':popular,'categories':categories,'unique':unique})

def blog(request):
    popular = words.objects.filter(popular=True)
    blogs = words.objects.all()
    books = words.objects.all()
    unique = []
    uniquetags = []
    for book in books:
        if book.tags in uniquetags:
            pass
        else:
            unique.append(book)
            uniquetags.append(book.tags)
    return render(request,"blog.html",{'blogs':blogs,'popular':popular,'unique':unique,'categories':categories})

def archives(request):
    popular = words.objects.filter(popular=True)
    blogs = words.objects.all()
    return render(request,"archives.html",{'blogs':blogs,'popular':popular})

