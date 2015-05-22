from django.contrib import admin
from polls.models import Question, Choice, Runner, Run
# Register your models here.

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class RunInline(admin.TabularInline):
  model = Run
  extra = 3



class RunnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['start_date'], 'classes': ['collapse']}),
    ]
    inlines = [RunInline]
    list_display = ('name', 'start_date')
    list_filter = ['start_date']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Runner, RunnerAdmin)

