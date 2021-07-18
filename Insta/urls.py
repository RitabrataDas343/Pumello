from django.urls import path
from Insta.views import (PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike, UserDetailView, EditProfile, toggleFollow, addComment, ExploreView)

urlpatterns = [
   path('', PostsView.as_view(), name='posts'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('post/new/', PostCreateView.as_view(), name='make_post'),
   path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
   path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
   path('like', addLike, name='addLike'),
   path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
   path('user/edit/<int:pk>', EditProfile.as_view(), name='edit_profile'),
   path('togglefollow', toggleFollow, name='togglefollow'),
   path('comment', addComment, name='addComment'),
   path('explore', ExploreView.as_view(), name='explore'),
]