from django.db.models import Model
from rest_framework import serializers
from app.models import Employee

# # # All fields in serializers are shown in input & output field,
# # # if we want to see some of the fields only in output or input,
# # # output --> read_only=True
# # # input --> write_only=True
#
# class EmployeeSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     Name=serializers.CharField(max_length=20)
#     Empid=serializers.IntegerField()
#     Age=serializers.IntegerField()
#     Place=serializers.CharField(max_length=30)
#     gender_choices=(('male','Male'),('female','Female'))
#     Gender=serializers.ChoiceField(choices=gender_choices)
#     Joining_date=serializers.DateField(read_only=True)        #automatically adds current date to employee record
#     Salary=serializers.IntegerField()
#     Designation=serializers.CharField(max_length=20)
#
#     image=serializers.ImageField()
#
#     # create() is called after validation and before saving
#     def create(self, validated_data):
#         print(validated_data)       #data after validation
#         e=Employee.objects.create(**validated_data)
#         return e
#
#     # After validation before saving
#     def update(self,instance,validated_data):
#         instance.Name=validated_data.get('Name',instance.Name)
#         instance.Empid=validated_data.get('Empid',instance.Empid)
#         instance.Age=validated_data.get('Age',instance.Age)
#         instance.Place=validated_data.get('Place',instance.Place)
#         instance.Gender=validated_data.get('Gender',instance.Gender)
#         instance.Salary=validated_data.get('Salary',instance.Salary)
#         instance.Designation=validated_data.get('Designation',instance.Designation)
#
#         instance.save()
#         return instance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        read_only_fields=['id','joining_date']

    # def validate(self,data):
    #     if 'Age' in data:
    #         if data['Age']<=0:
    #             raise serializers.ValidationError("Age should be Positive")
    #     return data

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        return u