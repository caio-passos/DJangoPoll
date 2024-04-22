from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    """the code below helps parsing the question itself as string when called by a 
     Question.objects.all()
    """

    #modify the string return of its class when called.
    #this class will be identified as it's own question_text
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # if the last question was added within 24 hrs then returns true
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # has the exact same function as the above class
    def __str__(self):
        return self.choice_text
