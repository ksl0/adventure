from django import forms
import datetime
class NameForm(forms.Form):
  your_name = forms.CharField(label='Your name', max_length=100)

class RunForm(forms.Form):
  your_name = forms.CharField(label='Your name', max_length=100)
  dist = forms.FloatField(label="Miles ran", min_value=0.0, max_value=30.0)
  duration_minutes = forms.FloatField(label="time (minutes)", min_value=0, max_value=59)
  duration_hours= forms.FloatField(label="time (hours)", min_value=0, max_value=24)
  day = forms.DateField(initial=datetime.date.today)
  mood = forms.CharField(label="Mood", max_length=20)
   
  
