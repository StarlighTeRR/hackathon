from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    score = models.IntegerField()

class Result(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)