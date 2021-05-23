from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','pub_date']
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
