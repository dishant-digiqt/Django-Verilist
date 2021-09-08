from datetime import date
from rest_framework import serializers
import uuid
from .constants import status_choices, priority_choices


class ListSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    name = serializers.CharField(max_length=50, required=True)
    description = serializers.CharField(max_length=255, required=True)


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)
    priority = serializers.ChoiceField(choices=priority_choices, required=True)
    status = serializers.ChoiceField(choices=status_choices, required=True)
    due_date = serializers.DateField(required=True)
    completed_At = serializers.DateField(default=date.today)

# class MultiTaskSerializer(serializers.Serializer):
#     tasks = TaskSerializer(many=True)

#     def create(self, instance, validated_data):
#         multi_tasks = validated_data.pop('tasks', [])
#         instance = Task.objects.create(
#             title=validated_data.get('title', ''), 
#             description=validated_data.get('description', ''), 
#             status=validated_data.get('status', ''),
#             priority=validated_data.get('priority', ''),
#             due_date=validated_data.get('due_date', ''),
#             completed_At=validated_data.get('completed_At', '')
#         )
#         # task_data = Task.objects.create(**validated_data)
#         for task in multi_tasks:
#             task_data = Task.objects.get(id=task.get('id'))
#             instance.multi_tasks.add(task_data)
#         print(instance)
#         return instance


    # def create(self, validated_data):
    #     multi_tasks = validated_data.pop('tasks')
    #     task = Task.objects.create(**validated_data)
    #     for task in multi_tasks:
    #         Task.objects.get(**task)
    #     return task