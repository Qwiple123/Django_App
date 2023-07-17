from django.db import models
from django.contrib.auth.models import AbstractUser


class Test(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def logical_delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    QUESTION_TYPES = (
        ('Уникальный выбор', 'Уникальный выбор'),
        ('Множественный выбор', 'Множественный выбор'),
    )
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text



