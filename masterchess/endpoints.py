from django.conf.urls import include, url
from rest_framework import routers

from .api import GameViewSet, MoveViewSet, RegistrationApi, LoginAPI, UserAPI

router = routers.DefaultRouter()
router.register('games', GameViewSet, 'games')
router.register('move', MoveViewSet, 'moves')

urlpatterns = [
    url('^', include(router.urls)),
    url(r'^auth/register/$', RegistrationApi.as_view()),
    url(r'^auth/login/$', LoginAPI.as_view()),
    url(r'^auth/user/$', UserAPI.as_view()),
]