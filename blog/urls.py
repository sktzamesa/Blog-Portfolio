from django.urls import path
from . import views
from .feeds import LatestPostsFeeds
app_name = 'blog'

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    #path('',views.PostListView.as_view(),name='post_list'),
    path('<int:post_id>/share/',views.post_share,name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('comment/<int:post_id>',views.post_comment,name='post_comment'),
    path('search/',views.post_search,name='post_search'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('feed/',LatestPostsFeeds(),name='post_feed'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
