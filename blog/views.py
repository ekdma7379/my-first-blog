from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte = timezone.now())
    qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
    })

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk);
    # except Post.DoesnotExist:
    #     raise Http404 Page Not Found : from django.http import
    # 위랑 아래랑 같은 것이다. import get_object_or_404을 해야한다.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{
        'post' : post,
    })
# @login_required -> admin에서 로그아웃을 해버리면  post.author을 가져올 수가 없다. 그때를 방지하는 어노테이션 같은것
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {
            'form' : form,
    })

def post_edit(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk);
    # except Post.DoesnotExist:
    #     raise Http404 Page Not Found : from django.http import
    # 위랑 아래랑 같은 것이다. import get_object_or_404을 해야한다.
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html',{
        'form' : form,
    })