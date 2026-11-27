
from rest_framework import serializers
from app.models import Movie
# from django.contrib.auth.models import User
from django.core.mail import send_mail

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie

        fields="__all__"


# Using APIView
from app.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password',
                'email','first_name',
                'last_name','phone','address']

    def create(self,validated_data):
        u=CustomUser.objects.create_user(**validated_data)
        #To encrypt the password / password hashing we redefine create() in our UserSeroalizer class

        # For creating a user account
        # User.objects.create_user(**validated_data),automatically it will encrypt the password

        # For creating a superuser
        # User.objects.create_superuser(**validated_data) ,automatically it will create user as admin

        u.save()

        send_mail(

            subject="Welcome to our App",
            message="Thank you for signing up for an account",
            from_email="archanaasokan05@gmail.com",
            recipient_list=[u.email,],
            fail_silently=True
        )


        return u
