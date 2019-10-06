from django.db import models

class Question(models.Model):
    title = models.Charfield('name question', max_length = 100)
    text = models.TextField('text question')
    added_at = models.DateTmeField('date added question')
    rating = models.IntegerField('rating of question')
    author = models.Charfield('name author of question', max_length = 50)
    likes = models.Integer('number of likes of question')


class Answer(models.Model):
    text = models.TextField('text answer')
    added_at = models.DateTmeField('date added answer')
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.Charfield('name author of answer', max_length = 50)

