from django.urls import path
from .views import ArticleListCreateView, CommentListView, ArticleDetailView, CreateCommentToArticleView, \
    CreateReplyCommentView, ArticleBeforeThirdLevelCommentsView, ThirdLevelCommentsView, schema_view

urlpatterns = [
    path("article/all", ArticleListCreateView.as_view()),
    path("article/<int:pk>", ArticleDetailView.as_view()),
    path("article/3level-comment/<int:pk>", ArticleBeforeThirdLevelCommentsView.as_view()),
    path("comment/all", CommentListView.as_view()),
    path("comment/add/to-article", CreateCommentToArticleView.as_view()),
    path("comment/add/to-comment", CreateReplyCommentView.as_view()),
    path("comment/3-level", ThirdLevelCommentsView.as_view()),
    path("docs/", schema_view),
]
