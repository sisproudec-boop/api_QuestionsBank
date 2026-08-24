from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from PIL import Image
import os

class Asignature(models.Model):
    id = models.AutoField(primary_key=True)
    nameAs = models.CharField(max_length=100)

    def __str__(self):
        return self.nameAs

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    idAsignature = models.ForeignKey(Asignature, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    options = models.TextField()
    correctOption = models.TextField()

    def __str__(self):
        return self.question

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    idAsignature = models.ForeignKey('Asignature', on_delete=models.CASCADE, null=True, blank=True)
    content = CloudinaryField('image', folder='materials/', null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)

    def __str__(self):
        asignature_name = self.idAsignature.nameAs if self.idAsignature else "Sin asignatura"
        return f"(ID: {self.id}) - {asignature_name}"

    def clean(self):
        if not self.content and not self.text_content:
            raise ValidationError('Debes subir al menos una imagen o ingresar texto.')

class QuestionMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    idQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    idMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question {self.idQuestion.id} - Material {self.idMaterial.id}"