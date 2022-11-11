from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    profile_image = ProcessedImageField(
        upload_to="profile_images/",
        blank=True,
        processors=[ResizeToFill(120, 120)],
        format="JPEG",
        options={"quality": 60},
    )
