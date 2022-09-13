from django.urls import path
from . import views
from .views import AddPost, UpdatePost, DeletePost


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.postpage , name='postview'),
    path('createpost', AddPost.as_view(), name='createpost'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='editpost'),
    path('post/<int:pk>/deletepost', DeletePost.as_view(), name='deletepost'),
    path('search/', views.searchquery, name='search'),
]


