from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/post_media/{1}'.format(instance.post.user.id, filename)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    likes = models.IntegerField()
    caption = models.TextField(max_length=500)

    def __str__(self):
        return f"post - {self.id}"


# Create your models here.
class MediaFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"media - {self.id}"
