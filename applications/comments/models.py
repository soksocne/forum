from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.question.models import Question
User = get_user_model()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='comments')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=100)
    problem = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])
    image = models.ImageField(upload_to='', blank=True)
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
