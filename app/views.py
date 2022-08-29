from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect  
from .forms import EmployeeForm
from .models import Employee, Posts
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def index(request):
#
def index(request):
    posts = Posts.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 1)  # creating a paginator object
    # getting the desired page number from url
    page_number = 1
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', context)


# def index(request):
#     post = Posts.objects.all()
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(post, 10)
#     try:
#         post = paginator.page(page)
#     except PageNotAnInteger:
#         post = paginator.page(1)
#     except EmptyPage:
#         post = paginator.page(paginator.num_pages)
#
#     return render(request, 'post_list.html', { 'post': post })


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)
        print(form.is_valid())
        print("hello")
        
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except Exception as e:
                print(e)  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request, 'forms.html', {'form': form})
    

def show(request):  
    employees = Employee.objects.all()  
    return render(request, "show.html", {'employees': employees})
    

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request, 'edit.html', {'employee': employee})
    

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})
    

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")


def new_post(request):
    if request.method == "POST":
        print("ghej")
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_post')
            except Exception as e:
                print(e)
                pass
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})


def show_post(request):
    posts = Posts.objects.all()
    p = Paginator(posts, 1)  # creating a paginator object
    # getting the desired page number from url
    page_number = 1
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
        print(page_obj)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', {'posts': posts})
    # return render(request, "post_list.html", {'posts': posts}, context)


def edit_post(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'edit_post.html', {'post': post})


def update_post(request, id):
    print('enter')
    post = Posts.objects.get(id=id)
    print(post)
    form = PostForm(request.POST, instance=post)
    for field in form:
        print("Field Error:", field.name, field.errors)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/show_post")
    print('render')
    return render(request, 'edit_post.html', {'post': post})


def destroy_post(request, id):
    post = Posts.objects.get(id=id)
    post.delete()
    return redirect("/show_post")


