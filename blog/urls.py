from django.urls import path

from blog.views.post import PostViewSet
from blog.views.comment import CommentViewSet

urlpatterns = [
    path('post/',PostViewSet.as_view({'post':'create','get':'list'}),name='postviewset'),
    path('comment/',CommentViewSet.as_view({'post':'create'}),name='commentviewset')
]