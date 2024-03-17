from django.urls import include, path
from .views import GameCategoryViewSet, GameViewSet, ReferenceViewSet, ImageViewSet, VideoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'game-categories', GameCategoryViewSet,
                basename='gamecategory')
router.register(r'games', GameViewSet, basename='game')
router.register(r'references', ReferenceViewSet, basename='reference')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = [
    path('', include(router.urls)),
]
