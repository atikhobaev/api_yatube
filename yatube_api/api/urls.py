from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='token-auth'),
]
