from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    uploader = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    disLikes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    download = models.BooleanField(default=False)
    embed_code = models.TextField(default='')
    channel_name = models.CharField(max_length=255, default='Zee Music Company')
    channel_thumbnail = models.CharField(max_length=255, default='https://images.unsplash.com/photo-1532074205216-d0e1f4b87368?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAyfHx1c2VyfGVufDB8fDB8fHww')
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=255, default='', blank=True, null=True)
    descriptionHeading = models.CharField(max_length=255, default='', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)

class UserInteraction(models.Model):
    LIKE_CHOICES = [
        ('LIKE', 'Like'),
        ('DISLIKE', 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    likes = models.CharField(max_length=7, choices=LIKE_CHOICES, default=None, blank=True, null=True)
    shares = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.video.title}'
    
all_users = User.objects.all()

# class Video(models.Model):
#     # youtube_link = models.URLField()
#     title = models.CharField(max_length=255)
#     uploader = models.CharField(max_length=255)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     likes = models.IntegerField(default=0)
#     disLikes = models.IntegerField(default=0)
#     shares = models.IntegerField(default=0)
#     comments = models.IntegerField(default=0)
#     download = models.BooleanField(default=False)
#     embed_code = models.TextField(default='')
#     channel_name = models.CharField(max_length=255, default='Zee Music Company')
#     channel_thumbnail = models.CharField(max_length=255, default='https://images.unsplash.com/photo-1532074205216-d0e1f4b87368?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAyfHx1c2VyfGVufDB8fDB8fHww')
#     views = models.IntegerField(default=0)
#     tags = models.CharField(max_length=255, default='', blank=True, null=True)
#     descriptionHeading = models.CharField(max_length=255, default='', blank=True, null=True)
#     description = models.TextField(default='', blank=True, null=True)
    
# class UserInteraction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)
#     likes = models.BooleanField(default=False)
#     shares = models.BooleanField(default=False)
#     comments = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.video.title}'

