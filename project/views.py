from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions

from user_account.permissions import IsProjectOwner, IsCommentOwner

from .models import (
    Project,
    ProjectMember,
    Task,
    Comment
)
from .serializers import (
    ProjectSerializer,
    ProjectMemberSerializer,
    TaskSerializer,
    CommentSerializer
)


class ListCreateProject(generics.ListCreateAPIView):
    """
    Retrieve a list of all projects.
    Create a new project
    """
    model = Project
    queryset = Project.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ProjectSerializer
    
    
class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update details of a specific project.
    Delete a specific project
    Must be called by project owner
    """
    model = Project
    permission_classes = (IsProjectOwner, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = "id"
    

class ListCreateTask(generics.ListCreateAPIView):
    """
    Retrieve a list of all tasks in a project.
    Create a new task for a specific project
    """
    model = Task
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs.get("project_id"))
        queryset = Task.objects.filter(project=project)
        return queryset


class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update details of a specific task.
    Delete a specific task
    """
    model = Task
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"
    
    
class ListCreateComment(generics.ListCreateAPIView):
    """
    Retrieve a list of all comments on a task.
    Create a new comment on a task
    """
    model = Comment
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs.get("task_id"))
        queryset = Comment.objects.filter(task=task)
        return queryset
        

class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/Update details of a specific comment.
    Delete a specific comment
    Must be called by comment owner
    """
    model = Comment
    permission_classes = (permissions.IsAuthenticated, IsCommentOwner, )
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "id"