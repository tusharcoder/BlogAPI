from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
    class Meta:
        model=Post
        fields=(
            'title', 
            'description', 
            # comments
            # nested created by user
        )