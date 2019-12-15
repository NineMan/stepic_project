from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new():
        return self.order_by('-added_at')
    def popular():
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=100, default="")
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', on_delete=models.CASCADE)
    likes  = models.ManyToManyField(User, related_name='question_likes', blank=True)

    class Meta:
        db_table = "qa_questions" 
        ordering = ('added_at',)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.pk})


class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name='answer_author', on_delete=models.CASCADE)

    class Meta:
        db_table = "qa_answers"

    def __str__(self):
        return self.text

    def get_url(self):
        return reverse('answer', kwargs={'answer_id': self.pk})
