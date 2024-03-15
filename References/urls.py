from django.urls import include, path
from .views import GameCategoryViewSet, GameViewSet, ReferenceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'game-categories', GameCategoryViewSet,
                basename='gamecategory')
router.register(r'games', GameViewSet, basename='game')
router.register(r'references', ReferenceViewSet, basename='reference')

urlpatterns = [
    path('', include(router.urls)),
]
