from rest_framework import serializers


def validate_parent_comment(self_object):
    try:
        parent = self_object.request.data['parent_comment']
    except KeyError:
        raise serializers.ValidationError({"parent_comment": "This field is required."})
    for ins in self_object.queryset.all():
        if ins.id == parent:
            return ins.article


def validate_article_exist(self_object):
    try:
        self_object.request.data['article']
    except KeyError:
        raise serializers.ValidationError({"article": "This field is required."})
