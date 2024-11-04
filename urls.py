from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-blog/', add_blog, name="add_blog"),
    path('blog-detail/<slug>', blog_detail, name="blog_detail"),
    path('see-blog/', see_blog, name="see_blog"),
    path('blog-delete/<id>', blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', blog_update, name="blog_update"),
    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify"),
    path('contact-us/', contact_uss, name="contact_uss"),
    path('category-detail/<slug>', category_detail, name="category_detail"),
    path('add-category/', add_category, name="add_category"),
    #path('categories_blog/', categories_blog, name="categories_blog"),
    path('category/<str:cate>/', category_view, name="category"),
    path('search-blog/',search_view, name="search_view"),
    path('submit_review/<int:Blog_id>/',submit_review, name="submit_review"),
    path('see-category/', see_category, name="see_category"),
    path('comments/<id>',get_comments, name="get_comments"),
    path('request-category/', request_category, name="request_category")
    


]
