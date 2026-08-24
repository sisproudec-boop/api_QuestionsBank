from rest_framework import viewsets
from .models import Question, Material, QuestionMaterial, Asignature
from .serializer import QuestionSerializer, MaterialSerializer, QuestionMaterialSerializer, AsignatureSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter

# Definición de los viewsets
router = SimpleRouter()
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class QuestionMaterialViewSet(viewsets.ModelViewSet):
    queryset = QuestionMaterial.objects.all()
    serializer_class = QuestionMaterialSerializer

class AsignatureMaterialViewSet(viewsets.ModelViewSet):
    queryset = Asignature.objects.all()
    serializer_class = AsignatureSerializer

# Clase combinada para la API
class CombinedAPIView(APIView):
    def get(self, request):
        return Response({
            "questions": "https://zn4zz9nw-8090.use2.devtunnels.ms/api/v1/questions/",
            "materials": "https://zn4zz9nw-8090.use2.devtunnels.ms/api/v1/materials/",
            "question_materials": "https://zn4zz9nw-8090.use2.devtunnels.ms/api/v1/question_materials/",
            "asignatures": "https://zn4zz9nw-8090.use2.devtunnels.ms/api/v1/asignatures/",
        })
