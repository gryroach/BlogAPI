from django.db.models import Prefetch

from ..models import Comment, Article


comments = Comment.objects.prefetch_related(
            Prefetch(
                "reply_comment",
                queryset=Comment.objects.prefetch_related(
                    Prefetch(
                        "reply_comment",
                        queryset=Comment.objects.prefetch_related(
                            Prefetch(
                                "reply_comment",
                                queryset=Comment.objects.prefetch_related('reply_comment').all()
                                    )).all()
                            )).all(),
                    )).all()

articles = Article.objects.prefetch_related(
    Prefetch("comments",
             queryset=comments)
)
