from django.shortcuts import render , get_object_or_404

from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 3)           # هيعرض 3 بوستات فقط فى كل صفحه
    page_number = request.GET.get('page', 1)      # خلى رقم اول صفحه بشكل افتراضى 1
    try:                                          # تراى هنا علشان لو كتب فى الشريط فوق رقم صفحه مش موجود ميديش ايرور ويجبله اخر صفحه
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:                        # وده اكسبشن تانى علشان لو كتب حروف يرجعنى لاول صفحه مثلا
        posts = paginator.page(1)

    return render(request, 'blog/post/list.html', {'posts' : posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post' : post})


