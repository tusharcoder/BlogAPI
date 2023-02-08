from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract=True

class TimeFieldsMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract=True


class Post(BaseModel, TimeFieldsMixin, CreatedByMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(BaseModel, TimeFieldsMixin, CreatedByMixin):
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()

    def __str__(self) -> str:
        return F"{self.pk-self.post.pk-self.created_by.pk}"
