from django.contrib import admin

from .models import Test,Question,Answer

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title','author']


@admin.register(Question)
class Questiondmin(admin.ModelAdmin):
    list_display = ['test','text']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question','text','is_correct']
