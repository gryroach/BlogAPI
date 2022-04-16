from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

from .serializers import ArticleSerializer, CommentSerializer, CommentReplySerializer, CommentArticleSerializer
from .models import Article, Comment
from .src.comment_service import validate_parent_comment, validate_article_exist


class ArticleListCreateView(ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# api_view(['POST'])
# def create_comment_to_article_view(request, id=None):
#     try:
#         article = Article.objects.get(pk=id)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)A
#
#     if request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCommentToArticleView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentArticleSerializer

    def perform_create(self, serializer):
        validate_article_exist(self)
        serializer.save()


class CreateReplyCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReplySerializer

    def perform_create(self, serializer):
        article = validate_parent_comment(self)
        serializer.save(article=article)


class CommentListView(ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


schema_view = get_swagger_view(title='Blog API')
