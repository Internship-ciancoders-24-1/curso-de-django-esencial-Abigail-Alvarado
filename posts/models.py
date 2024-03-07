from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)
    tittle = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    def __srt__(self):
        return '{} by @{}'.format(self.tittle(), self.user.username)