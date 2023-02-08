from rest_framework import serializers
from blog.models import Post
from blog.serializers.comment import CommentSerializer, CommentReadSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentReadSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
    class Meta:
        model=Post
        fields=(
            'title', 
            'description', 
            'comments',
            'id',
            # nested created by user
        )