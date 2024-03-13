from django.urls import include, path
from .views import GameCategoryViewSet, GameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'game-categories', GameCategoryViewSet,
                basename='gamecategory')
router.register(r'games', GameViewSet, basename='game')

urlpatterns = [
    path('', include(router.urls)),
]
