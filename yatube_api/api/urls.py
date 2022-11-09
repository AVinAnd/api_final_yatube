from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_id>[1-9]\d*)/comments',
                   CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
