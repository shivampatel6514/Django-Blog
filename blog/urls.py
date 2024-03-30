from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.PostList, name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),

]
