from django.shortcuts import render,redirect
from . import forms,models

from django.contrib.auth.decorators import login_required
# Create your views here.

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



# @login_required
# def add_post(request):
#     if request.method =="POST":
#         post_form=forms.PostForm(request.POST)

#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect("homepage")
#     else:
#         post_form=forms.PostForm()

#     return render(request, 'add_post.html',{'form':post_form})


# using class based View
@method_decorator(login_required,name='dispatch')
class AddpostUsingCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# @login_required
# def edit_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     post_form=forms.PostForm(instance=post)
#     # print(post.title)
#     if request.method =="POST":
#         post_form=forms.PostForm(request.POST,instance=post)

#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect("homepage")
#     return render(request, 'add_post.html',{'form':post_form})

# edit post using class base view
@method_decorator(login_required,name='dispatch')
class EditPostUpdateView(UpdateView):
    model= models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')



# @login_required
# def delete_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect("homepage")


# delete post usign calss base view
@method_decorator(login_required,name='dispatch')
class DeletePostDeleteView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


class DetailPostView(DetailView):
    model = models.Post

    pk_url_kwarg = 'id'
    template_name = 'post_dtls.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()

        
        comment_form = forms.CommentForm()
            

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

