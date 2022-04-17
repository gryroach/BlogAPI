from rest_framework import serializers
from .models import Article, Comment


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    reply_comment = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "owner", "created", "text", "article", "parent_comment", "reply_comment")


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "content", "comments")


class CommentReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("owner", "text", "parent_comment")


class CommentArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("owner", "text", "article")
