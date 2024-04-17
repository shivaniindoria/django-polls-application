from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question_text", "pub_date", "was_published_recently"]
    search_fields = ["question_text"]
    list_filter = ["pub_date"]
    # list_per_page = 2
    fieldsets = [
        (None, {
            "fields": ['question_text']
        }),
        ('date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    

admin.site.register(Question, QuestionAdmin)
