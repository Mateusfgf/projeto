from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm, ContatoForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bforum/post_list.html', {'posts': posts})
    post.visits += 1
    post.save()

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.visits += 1
    post.save()
    return render(request, 'bforum/post_detail.html', {'post': post})

@login_required
def post_new(request):
   
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'bforum/post_new.html', {'form': form})


    
    # try:
    #     post = Post.objects.get(pk=pk) 
        
        
    # except Post.DoesNotExist:
    #     return redirect('post_list')
    # # post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.filter(visita=+0)
    # post.visita += 1
    # post.save()
    
@login_required    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bforum/post_edit.html', {'form': form})

    def post_erro404(request):
        
        return HttpResponse("Hello, world..")


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'bforum/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bforum/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            Remetente = email_form.cleaned_data['Remetente']
            Titulo = email_form.cleaned_data['Titulo']
            Texto = email_form.cleaned_data['Texto']

            try:
                send_mail(Titulo, Texto, Remetente, ['mateusowmedeiros@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('post_list')
    return render(request, 'bforum/email.html', {'form': email_form})

# 