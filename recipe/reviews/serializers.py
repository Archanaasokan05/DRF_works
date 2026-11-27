from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from accounts.serializers import UserSerializer
from recipies.serializers import RecipieSerializer
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # # Nested Serializer
    # user=UserSerializer(read_only=True)
    # recipe=RecipieSerializer(read_only=True)
    # # displays the full details(all fields) of related objects


    # # StringRelatedField
    # user=StringRelatedField()
    # recipe=StringRelatedField()
    # # Displays the related objects using its string representation as defined inside __str__()


    message=serializers.SerializerMethodField()

    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=['user','created_at']

    def get_message(self,obj):
        return "hello"

    def get_user(self,obj):
        return obj.user.email

    def get_recipe(self,obj):
        return obj.recipe.recipe_name
