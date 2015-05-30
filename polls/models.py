# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from geoposition.fields import GeopositionField

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __unicode__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0) 
  def __unicode__(self):
    return self.choice_text 
 
class Runner(models.Model):
  name = models.CharField(max_length=200)
  start_date = models.DateTimeField('date published', auto_now=True)
  def __unicode__(self):
    return self.name


class Run(models.Model):
  person = models.ForeignKey(Runner)
  distance = models.DecimalField(max_digits=5, decimal_places=2)
  time = models.DecimalField(max_digits=5, decimal_places=2) #minutes
  mood = models.CharField(max_length = 200)
  rgb = models.CharField(max_length=20)
  position= GeopositionField()
  def __unicode__(self):
    return self.person.name
