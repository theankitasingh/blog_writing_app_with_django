from django.shortcuts import render, redirect , get_object_or_404
from .form import *
from django.contrib.auth import logout 
from django.db.models import Q
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('/login/')

def home(request):
    contexts = {'blogs': deardiaryModel.objects.all(),'cat_menu':categorymodel.objects.all(), 'rating':ReviewRating.objects.all()}
    
    return render(request, 'home.html', contexts)
    def get_context_data(self,*args,**kwargs):
        cat_menu=categorymodel.objects.all()
        context= super(home,self).get_context_data(*args,**kwargs)
        context["cat_menu"]= cat_menu
        return context


def login_view(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = deardiaryModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)



@login_required(login_url='/login/')
def category_detail(request, slug):
    context = {}
    try:
        category_posts=categorymodel.objects.filter(slug=slug).first()
        context['category_posts'] = category_posts

    except Exception as e:
        print(e)
    return render(request, 'category_detail.html', context)


@login_required(login_url='/login/')
def see_blog(request):
    context = {}

    try:
        blog_objs = deardiaryModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blogs.html', context)

def see_category(request):
    context = {}

    try:
        blog_objs = requestcat.objects.all()
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_categorys.html', context)

@login_required(login_url='/login/')
def request_category(request):
    context = {'form': BloggFormm}
    try:
        if request.method == 'POST':
            form = BloggForm(request.POST)
            print(request.FILES)
            name = request.POST.get('name')
            user = request.user
            
            
            if form.is_valid():
                print('Valid')
                

            blog_obj = requestcat.objects.create(
                name=name, user=user 
            )
            print(blog_obj)
            return redirect('add_blog')
    except Exception as e:
        print(e)

    return render(request, 'request_category.html', context)

@login_required(login_url='/login/')
def add_category(request):
    context = {'form': BloggForm}
    try:
        if request.method == 'POST':
            form = BloggForm(request.POST)
            print(request.FILES)
            name = request.POST.get('name')
            
            if form.is_valid():
                print('Valid')
                

            blog_obj = categorymodel.objects.create(
                name=name
            )
            print(blog_obj)
            return redirect('add_blog')
    except Exception as e:
        print(e)

    return render(request, 'add_category.html', context)



@login_required(login_url='/login/')
def add_blog(request):
    context = {'form' : BlogForm } #'form_2': BloggForm 

    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            # form_2 = BloggForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user
            #cate=request.POST['cate']
            # categories=request.POST.get('categories')
            
            category=request.POST.get('category')
            if form.is_valid() : #,form_2.is_valid()
                print('Valid')
                content = form.cleaned_data['content']
                
            blog_obj = deardiaryModel.objects.create(
                user=user, title=title,
                content=content, image=image , category=category 
            )
            print(blog_obj)
            return redirect('/')
    except Exception as e:
        print(e)

    return render(request, 'add_blogs.html', context)


@login_required(login_url='/login/')
def blog_update(request, slug):
    context = {}
    try:
        blog_obj = deardiaryModel.objects.get(slug=slug)

        # Ensure only the owner can update the blog
        if blog_obj.user != request.user:
            return redirect('/')

        # Initialize the form with the current blog content
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)

        # Handle the form submission
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)  # Pass both POST data and files
            image = request.FILES.get('image')  # Use get() to safely access the file
            title = request.POST.get('title')   # Get the title from POST data
            categories = request.POST.get('categories')  # Get the categories from POST data
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

                # Update the blog object with new data
                blog_obj.title = title
                blog_obj.content = content
                if image:
                    blog_obj.image = image  # Update image only if new image is uploaded
                blog_obj.categories = categories
                blog_obj.save()  # Save the changes

                return redirect('/')  # Redirect after successful update

        # Pass the existing blog and form to the context
        context['blog_obj'] = blog_obj
        context['form'] = form

    except Exception as e:
        print(e)  # Log the error for debugging

    return render(request, 'update_blog.html', context)


@login_required(login_url='/login/')
def blog_delete(request, id):
    try:
        blog_obj = deardiaryModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')


def register_view(request):
    
    return render(request, 'register.html')

def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')

def contact_uss(request):
    return render(request, 'contact_us.html')

@login_required(login_url='/login/')
def category_view(request, cate):
    
    category_posts=deardiaryModel.objects.filter(category=cate)

    return render(request, 'categories.html',{'cate': cate,'category_posts':category_posts})

# @login_required(login_url='/login/')
def search_view(request):
    contexts=deardiaryModel.objects.all()
    if request.method == "POST":
        search=request.POST['search']
        blog_obj=deardiaryModel.objects.filter(
            Q(title__contains=search)|
            Q(content__contains=search)|
            Q(category__contains=search)|
            Q(user__username__contains=search)
            )
        return render(request, 'search.html', {'search':search,'blog_obj':blog_obj,'contexts':contexts})
    else:
        return render(request, 'search.html', {})
@login_required(login_url='/login/')
def submit_review(request,Blog_id):
    url= request.META.get('HTTP_REFERER')
    if request.method=="POST":
        try:
            reviews= ReviewRating.objects.get(user__id=request.user.id, Blog__id=Blog_id)
            form= BloggFForm(request.POST, instance=reviews)
            form.save()
            messages.success(request,'Thanks you! Review updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist :

            form= BloggFForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.rating=form.cleaned_data['rating']
                data.review=form.cleaned_data['review']
                data.ip=request.META.get('REMOTE_ADDR')
                data.Blog_id=Blog_id
                data.user_id=request.user.id
                data.save()
                messages.success(request,'Thanks you! Review added.')
                return redirect(url)

@login_required(login_url='/login/')
def get_comments(request, id):
    data=deardiaryModel.objects.get(id=id)
    comment=ReviewRating.objects.all().filter(Blog_id= id)
    return render(request, 'comments.html' , {'data':data, 'comments':comment})