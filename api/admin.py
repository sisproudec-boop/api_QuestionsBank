from django.contrib import admin
from .models import Question, Material, QuestionMaterial, Asignature

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionMaterial)
admin.site.register(Material)
admin.site.register(Asignature)