from rest_framework import serializers

from .models import (
    Project,
    ProjectMember,
    Task,
    Comment
)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "owner",
        )
        
        
class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = (
            "id",
            "project",
            "user",
            "role"
        )
        
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "status",
            "priority",
            "assigned_to",
            "project",
            "created_at",
            "updated_at",
            "due_date",
        )
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "user",
            "task"
        )