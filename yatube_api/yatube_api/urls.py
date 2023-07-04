from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from rest_framework import routers
from api.views import (PostViewSet,
                       GroupList,
                       GroupDetails,
                       CommentList,
                       CommentEdit)

router = routers.DefaultRouter()
router.register('api/v1/posts/', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/', include(router.urls)),
    path('api/v1/groups/', GroupList.as_view(),
         name='groups'),
    path('api/v1/groups/{group_id}/', GroupDetails.as_view(),
         name='groups_detail'),
    path('api/v1/posts/{post_id}/comments/', CommentList.as_view(),
         name='post_comments'),
    path('api/v1/posts/{post_id}/comments/{comment_id}/',
         CommentEdit.as_view(),
         name='comments_edit'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
