from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


class ArticleDetailView(ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentDetailView(ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
