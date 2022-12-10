from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts/', views.PostList, name='posts'),
    path('posts/new/', views.NewPost.as_view(), name='posts/new'),
    path('posts/<int:pk>/edit', views.UpdatePost.as_view(), name='posts/update'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('posts/<int:pk>/new_comment', views.NewComment.as_view(), name='comments/new'),
    path('comments/<int:pk>', views.delete_comment, name='delete-comment'),

]