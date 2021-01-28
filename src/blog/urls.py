from django.urls import path
from .views import CategoryList, CommentCreate, PostList, PostDetail, PostCreate, PostUpdate, PostDelete, UserPostList

urlpatterns = [
    path("", CategoryList.as_view(), name="category_list"),
    path("list/", PostList.as_view(), name="post_list"),
    path("postlist/", UserPostList.as_view(), name="user_list"),
    path("create/", PostCreate.as_view(), name="post_create"),
    path("detail/<slug>/", PostDetail.as_view(), name="post_detail"),
    # path("like/<slug>/", PostCreate.as_view(), name="post_like"),
    path("update/<slug>/", PostUpdate.as_view(), name="post_update"),
    path("delete/<slug>/", PostDelete.as_view(), name="post_delete"),
    path("comment/<slug>/", CommentCreate.as_view(), name="create_comment")
]