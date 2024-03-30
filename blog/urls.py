from django.urls import include, path

from . import views
# from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    # path("feed/rss", LatestPostsFeed(), name="post_feed"),
    # path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList, name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),

]
