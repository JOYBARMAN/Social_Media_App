"""Urls for post reaction"""

from django.urls import path
from post_reaction.rest.views.post_reaction import (
    PostReactionCount,
    PostReactionCreate,
    PostCommentList,
)

urlpatterns = [
    path(
        "/count",
        PostReactionCount.as_view(),
        name="user-post-reaction-count",
    ),
    path(
        "",
        PostReactionCreate.as_view(),
        name="user-post-reaction-create",
    ),
    path(
        "/comment",
        PostCommentList.as_view(),
        name="user-post-comment",
    ),
]
