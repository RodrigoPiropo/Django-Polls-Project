from django.db import models
from django.db.models import Max


class Question(models.Model):
    question_text = models.TextField()

    option1 = models.CharField(max_length=20)
    option1_votes = models.IntegerField(default=0)
    option2 = models.CharField(max_length=20)
    option2_votes = models.IntegerField(default=0)
    option3 = models.CharField(max_length=20)
    option3_votes = models.IntegerField(default=0)

    date_added = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.option1_votes + self.option2_votes+ self.option3_votes

    def __str__(self):
        return self.question_text
