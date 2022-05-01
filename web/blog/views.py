from django.db.models import Prefetch
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view

from .serializers import ArticleSerializer, CommentSerializer, \
    CommentReplySerializer, CommentArticleSerializer
from .models import Article, Comment
from .services.comment_service import filter_result_of_article, \
    filter_third_level_comment, filter_comments, add_reply_to_comment
from .services.validators import validate_parent_comment


class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.prefetch_related(Prefetch(
        "comments", queryset=Comment.objects.all()))
    serializer_class = ArticleSerializer


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        article_data = ArticleSerializer(article).data
        comment_data = CommentSerializer(Comment.objects.filter(article__id=pk),
                                         many=True).data
        comments = add_reply_to_comment(comment_data)
        article_data["comments"] = filter_comments(comments)
        return Response(article_data)


class ArticleBeforeThirdLevelCommentsView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        article_data = ArticleSerializer(article).data
        comment_data = CommentSerializer(Comment.objects.filter(article__id=pk),
                                         many=True).data
        article_data["comments"] = add_reply_to_comment(comment_data)
        response = filter_result_of_article(article_data)
        return Response(response)


class CreateCommentToArticleView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentArticleSerializer


class CreateReplyCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReplySerializer

    def perform_create(self, serializer):
        article = validate_parent_comment(self)
        serializer.save(article=article)


class CommentListView(APIView):
    def get(self, request):
        comment_data = CommentSerializer(Comment.objects.all(),
                                         many=True).data
        response = add_reply_to_comment(comment_data)
        return Response(response)


class ThirdLevelCommentsView(APIView):
    def get(self, request):
        comment_data = CommentSerializer(Comment.objects.all(),
                                         many=True).data
        comments = add_reply_to_comment(comment_data)
        response = filter_third_level_comment(comments)
        return Response(response)


schema_view = get_swagger_view(title='Blog API')
