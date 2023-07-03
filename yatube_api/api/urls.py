
from django.urls import include, path
from rest_framework.authtoken import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/v1/posts/', )

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('api/v1/groups/', name='groups'),
    path('api/v1/groups/{group_id}/', name='groups_detail'),
    path('api/v1/posts/{post_id}/comments/', name='post_comments'),
    path('api/v1/posts/{post_id}/comments/{comment_id}/', name='comments_edit'),

]
