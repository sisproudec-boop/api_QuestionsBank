from rest_framework import serializers
from .models import Question, Material, QuestionMaterial, Asignature

class MaterialSerializer(serializers.ModelSerializer):
    nameAs = serializers.CharField(source='idAsignature.nameAs', read_only=True)
    
    idAsignature = serializers.PrimaryKeyRelatedField(
        queryset=Asignature.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Material
        fields = ['id', 'idAsignature', 'nameAs', 'content', 'text_content']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.content:
            representation['content'] = instance.content.url
        return representation


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionMaterial
        fields = '__all__'


class AsignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignature
        fields = '__all__'