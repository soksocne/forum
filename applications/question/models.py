from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    title = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    problem = models.TextField()
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='like')
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like
