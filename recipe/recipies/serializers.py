from rest_framework import serializers
from recipies.models import Recipie

class RecipieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipie
        fields="__all__"