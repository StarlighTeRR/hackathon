from django.contrib import admin
from .models import Question, Answer, Result, Choice,User

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Choice)
admin.site.register(User)