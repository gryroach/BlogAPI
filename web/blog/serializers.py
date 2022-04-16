from rest_framework import serializers
from .models import Article, Comment


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reply_comment = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "owner", "created", "text", "article", "parent_comment", "reply_comment")


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "title", "content", "comments")
