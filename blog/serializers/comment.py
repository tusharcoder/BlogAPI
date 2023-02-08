from rest_framework import serializers
from blog.models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source='for_post_id',required=True)
    class Meta:
        model=Comment
        fields=(
            'comment_text', 
            'post_id'
            # nested post
        )
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        # validated_data['post'] = Post.objects.get(pk=validated_data.pop('post_id'))
        return super().create(validated_data)
    
class CommentReadSerializer(CommentSerializer):
    class Meta:
        model=Comment
        fields=('comment_text','id')