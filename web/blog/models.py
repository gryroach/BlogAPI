from django.db import models


class Article(models.Model):
    title = models.CharField("Title", max_length=255, blank=False)
    content = models.TextField("Content", blank=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['title']


class Comment(models.Model):
    owner = models.CharField("Name", max_length=255, blank=False)
    created = models.DateTimeField("Created", auto_now_add=True)
    text = models.TextField("Text", blank=True)
    article = models.ForeignKey(Article, related_name="comment", on_delete=models.CASCADE, blank=False)
    related_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.owner} {self.created}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['created']
