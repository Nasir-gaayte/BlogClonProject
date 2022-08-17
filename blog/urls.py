from django.urls import path
from blog import views


app_name = 'blog'


urlpatterns = [
     path('',views.PostListView.as_view(),name='post_list'),
     path('about/',views.AboutView.as_view(),name='about'),
     path('post/<pk>/detail',views.PostDetailView.as_view(),name='post_detail'),
     path('post/new/',views.CreatePostView.as_view(),name='post_new'),
     path('post/<pk>/update/',views.UpdatePostView.as_view(),name='post_update'),
     path('post/<pk>/remove/',views.PostDeleteView.as_view(),name='post_delete'),
     path('draft/',views.DraftListView.as_view(),name='post_draft'),
     path('post/<pk>/commit_form/',views.add_commit_to_post,name='commit_form'),
     path('comment/<pk>/approve/',views.comment_approve,name='comment_approve'),
     path('comment/<pk>/remove/',views.comment_remove,name='comment_remove'),
     path('post/<pk>/publish/',views.post_publish,name='post_publish'),
 
]
