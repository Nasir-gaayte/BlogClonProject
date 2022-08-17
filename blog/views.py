from email.policy import default
from time import timezone
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                  DeleteView,UpdateView,
                                  View,CreateView,DetailView)
from .models import Post,Comment
from django.urls import reverse_lazy


# Create your views here.
class AboutView(TemplateView):
    template_name= 'blog/about.html'

# def about(request):
#     return render(request,'blog/about.html')

class PostListView(ListView):
    modle = Post
    
    
    def get_queryset(self):
        return Post.objects.order_by('-published_date')
    
    
        
class PostDetailView(DetailView):
    model: Post
    
    
class CreatePostView(LoginRequiredMixin ,CreateView):
    
    login_url= 'login/'
    redirect_field_name= 'blog/post_detail.html'
    form_class = PostForm
    model = Post       
    
    
    
class UpdatePostView(LoginRequiredMixin, UpdateView): 
    login_url= 'login/'
    redirect_field_name= 'blog/post_detail.html'
    form_class = PostForm
    model = Post 
    
    
    
class PostDeleteView(LoginRequiredMixin ,DeleteView):
           model = Post
           success_url= reverse_lazy ('post_list')
           
           
           
           
class DraftListView(LoginRequiredMixin,ListView):
    login_url= 'login/'  
    redirect_field_name= 'blog/post_list.html'
    model = Post 
    
    def get_queryset(self):
         return Post.objects.filter(published_date__isnull=True).order_by('created_date')      

@login_required
def post_publish (request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)  
   
   
     
@login_required     
def add_commit_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect ('post_detail', pk=post.pk)
        else:
            form = CommentForm()
    return render(request,'blog/commit_form.html',{'form':form})  


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()  
    return redirect ('post_detail',pk=comment.post.pk)    
        
@login_required
def  comment_remove(request, pk):
    comment = get_object_or_404(comment,pk=pk)
    post_pk = comment.post.pk 
    comment.delete()
    return redirect('post_detail',pk= post_pk)   
    
     