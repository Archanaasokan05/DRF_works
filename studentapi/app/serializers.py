from django.db import models
from rest_framework import serializers
from app.models import Student

class StudentSerializer(serializers.Serializer):
    Name=serializers.CharField(max_length=30)
    Age=serializers.IntegerField()
    Course=serializers.CharField(max_length=30)
    Marks=serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)       #data after validation
        s=Student.objects.create(**validated_data)
        return s

    # After validation before saving
    def update(self,instance,validated_data):
        instance.Name=validated_data.get('Name',instance.Name)
        instance.Age=validated_data.get('Age',instance.Age)
        instance.Course=validated_data.get('Course',instance.Course)
        instance.Marks=validated_data.get('Marks',instance.Marks)

        instance.save()
        return instance
