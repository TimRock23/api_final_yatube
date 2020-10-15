from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet,
                basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/follow/', views.FollowList.as_view()),
    path('v1/group/', views.GroupList.as_view()),
]
