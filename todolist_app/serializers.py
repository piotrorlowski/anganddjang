from rest_framework import serializers

from .models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'