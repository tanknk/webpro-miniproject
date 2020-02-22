from django.shortcuts import render, redirect
from post.models import Post, Message
from post.forms import PostForm, MessageForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    search_txt_sell = request.GET.get("sellSearch")
    search_txt_buy = request.GET.get("buySearch")

    if(search_txt_sell and search_txt_buy is not None): #กรณีที่ค้นหา 2 ช่อง
        sell = Post.objects.filter(text_book__icontains=search_txt_sell).filter(type='S').filter(status="OPEN")
        buy = Post.objects.filter(text_book__icontains=search_txt_buy).filter(type='B').filter(status="OPEN")
    elif(search_txt_sell is not None and search_txt_buy is None): #กรณีที่ค้นหา ช่องขาย อย่างเดียว
        sell = Post.objects.filter(text_book__icontains=search_txt_sell).filter(type='S').filter(status="OPEN")
        buy = Post.objects.filter(type='B').filter(status="OPEN")
    elif(search_txt_sell is None and search_txt_buy is not None): #กรณีที่ค้นหา ช่องซื้อ อย่างเดียว
        sell = Post.objects.filter(type='S').filter(status="OPEN")
        buy = Post.objects.filter(text_book__icontains=search_txt_buy).filter(type='B').filter(status="OPEN")
    else: #กรณีไม่ค้นหาเลย
        sell = Post.objects.filter(type='S').filter(status="OPEN")
        buy = Post.objects.filter(type='B').filter(status="OPEN")
    
    context = {
        "sell" : sell,
        "buy" : buy
    }
    return render(request, 'post/index.html', context=context)

def post_list(request):
    post = Post.objects.filter(create_by__username=request.user)
    context = {
        "post" : post
    }
    return render(request, 'post/post_list.html', context=context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.create_by_id = request.user.pk
            book.save()
            return redirect('post_list')
    return render(request, 'post/add_post.html', { 'form' : PostForm })

def close_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.status = "CLOSE"
    post.save()
    return redirect('post_list')

def view_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Message.objects.filter(post_id_id=post.id)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.create_by_id = request.user.pk
            new_comment.post_id_id = post_id
            new_comment.save()
            redirect('view_post', post_id=post_id)

    if comment:
        context = {
            "post" : post,
            "comment" : comment,
            "form" : MessageForm,
        }
    else:
        context = {
            "post" : post,
            "form" : MessageForm
        }
    return render(request, 'post/view_post.html', context=context)
