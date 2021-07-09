from django.db import models
from django.contrib.auth.models import User
# from post.models import Post

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
from django.conf import settings
import os


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    # favorites = models.ManyToManyField(Post)
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Picture')

    def __str__(self):
        return self.user.username


class Following(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = [['follower', 'following']]

    def __str__(self):
        return f"{self.follower} - {self.following}"


# database signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
