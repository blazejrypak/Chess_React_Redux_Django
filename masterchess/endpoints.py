from django.conf.urls import include, url
from rest_framework import routers

from .api import GameViewSet, new_game, MoveViewSet

router = routers.DefaultRouter()
router.register('games', GameViewSet, 'game')
router.register('move', MoveViewSet, 'move')

urlpatterns = [
    url('^', include(router.urls)),
    url(r'^new_game/$', new_game),
]