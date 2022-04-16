from django.urls import path
from .views import ArticleDetailView, CommentDetailView

urlpatterns = [
    path("article/", ArticleDetailView.as_view()),
    path("comments/", CommentDetailView.as_view())
]
