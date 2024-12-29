from rest_framework import serializers
from .models import Tasks, Comments

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 'content', 'user', 'task', 'created_at']