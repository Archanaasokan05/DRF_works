from accounts.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password',
                'email','phone','bio']

    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
