from rest_framework.relations import StringRelatedField
from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    word_count=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields='__all__'
        read_only_fields=['id','author','created_at','updated_at']

    def get_word_count(self,obj):
        return len(obj.content.split())
