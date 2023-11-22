from django.urls import path
from post.rest.views.posts import (
    AdminPostList,
    UserPostList,
    UserPostCreate,
    UserPostDetail,
    UserPostUpdate,
)

urlpatterns = [
    path("", UserPostList.as_view(), name="user-post-list"),
    path("/admin", AdminPostList.as_view(), name="admin-post-list"),
    path("/add", UserPostCreate.as_view(), name="user-post-create"),
    path("/<uuid:uid>", UserPostDetail.as_view(), name="user-post-details"),
    path("/<uuid:uid>/update", UserPostUpdate.as_view(), name="user-post-update"),
]
