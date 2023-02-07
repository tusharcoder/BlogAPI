from django.urls import path

from blog.views.post import PostViewSet

urlpatterns = [
    path('post/',PostViewSet.as_view({'post':'create'}),name='postviewset')
]