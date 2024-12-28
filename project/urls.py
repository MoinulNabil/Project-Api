from django.urls import path

from .views import (
    ListCreateProject,
    RetrieveUpdateDestroyProject,
    ListCreateTask,
    RetrieveUpdateDestroyTask,
    ListCreateComment,
    RetrieveUpdateDestroyComment
)

urlpatterns = [
    path('projects/', ListCreateProject.as_view()),
    path('projects/<int:id>/', RetrieveUpdateDestroyProject.as_view()),
    path('projects/<project_id>/tasks/)', ListCreateTask.as_view()),
    path('tasks/<int:id>/', RetrieveUpdateDestroyTask.as_view()),
    path('tasks/<int:task_id>/comments/', ListCreateComment.as_view()),
    path('comments/<int:id>/', RetrieveUpdateDestroyComment.as_view())
]