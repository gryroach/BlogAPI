from django.urls import path
from .views import ArticleListCreateView, CommentListView, ArticleDetailView, CreateCommentToArticleView, \
    CreateReplyCommentView, schema_view

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view()),
    path("article/<int:pk>", ArticleDetailView.as_view()),
    path("comment/all", CommentListView.as_view()),
    path("comment/add/article", CreateCommentToArticleView.as_view()),
    path("comment/add/comment", CreateReplyCommentView.as_view()),
    path("docs/", schema_view)
]
