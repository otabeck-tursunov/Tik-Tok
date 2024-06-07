from django.db import models
from users.models import User


class Video(models.Model):
    TYPE_CHOICES = (
        ('private', 'private'),
        ('public', 'public'),
        ('friends', 'friends')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    video_path = models.FileField(upload_to='videos/')
    cover_path = models.ImageField(upload_to='covers/')
    music_path = models.FileField(upload_to='musics/')
    views = models.PositiveIntegerField(default=0)
    status_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    comments_allowed = models.BooleanField(default=True)
    comments_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    shares_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.caption


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'video'),)

    def __str__(self):
        return self.video


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'comment'),)

    def __str__(self):
        return self.comment


