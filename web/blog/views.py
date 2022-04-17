from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework_swagger.views import get_swagger_view

from .serializers import ArticleSerializer, CommentSerializer, CommentReplySerializer, CommentArticleSerializer
from .models import Article, Comment
from .src.comment_service import filter_result_of_article, filter_third_level_comment
from .src.validators import validate_parent_comment, validate_article_exist


class ArticleListCreateView(ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleBeforeThirdLevelCommentsView(RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = filter_result_of_article(response.data)
        return super().finalize_response(request, response, *args, **kwargs)


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


class ThirdLevelCommentsView(ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = filter_third_level_comment(response.data)
        return super().finalize_response(request, response, *args, **kwargs)


schema_view = get_swagger_view(title='Blog API')
