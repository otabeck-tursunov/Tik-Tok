from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('regular', 'regular'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user-profile/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"from {self.from_user.username} to {self.to_user.username}"

    class Meta:
        unique_together = (('from_user', 'to_user'),)


