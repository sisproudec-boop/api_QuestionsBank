from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    QuestionViewSet,
    MaterialViewSet,
    QuestionMaterialViewSet,
    AsignatureMaterialViewSet,
    CombinedAPIView
)

router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='question')
router.register('materials', MaterialViewSet, basename='materials')
router.register('question_materials', QuestionMaterialViewSet, basename='question-material')
router.register('asignatures', AsignatureMaterialViewSet, basename='asignature')

urlpatterns = [
    path('combined/', CombinedAPIView.as_view(), name='combined-api'),
    path('', include(router.urls)),
]