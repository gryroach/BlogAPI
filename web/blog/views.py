from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework_swagger.views import get_swagger_view

from .serializers import ArticleSerializer, CommentSerializer, CommentReplySerializer, \
    CommentArticleSerializer, ArticleListSerializer
from .models import Article, Comment
from .src.comment_service import filter_result_of_article, filter_third_level_comment, filter_comments
from .src.validators import validate_parent_comment
from .src.queries import comments, articles


class ArticleListCreateView(ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailView(RetrieveAPIView):

    queryset = articles
    serializer_class = ArticleSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data['comments'] = filter_comments(response.data['comments'])
        return super().finalize_response(request, response, *args, **kwargs)


class ArticleBeforeThirdLevelCommentsView(RetrieveAPIView):

    queryset = articles
    serializer_class = ArticleSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = filter_result_of_article(response.data)
        return super().finalize_response(request, response, *args, **kwargs)


class CreateCommentToArticleView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentArticleSerializer


class CreateReplyCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReplySerializer

    def perform_create(self, serializer):
        article = validate_parent_comment(self)
        serializer.save(article=article)


class CommentListView(ListAPIView):

    queryset = comments
    serializer_class = CommentSerializer


class ThirdLevelCommentsView(ListAPIView):

    queryset = comments
    serializer_class = CommentSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = filter_third_level_comment(response.data)
        return super().finalize_response(request, response, *args, **kwargs)


schema_view = get_swagger_view(title='Blog API')
