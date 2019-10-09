from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', on_delete=models.CASCADE)
    likes  = models.ManyToManyField(User, related_name='question_likes', blank=True)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name='answer_author', on_delete=models.CASCADE)

