from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']
