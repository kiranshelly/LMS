from django.contrib import admin
from Quiz.models import *


admin.site.register(MultipleChoiceModel)
admin.site.register(FillintheBlanksModel)
admin.site.register(TrueandFalseModel)

