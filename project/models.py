from django.db import models
from django.conf import settings


class TimeStamp(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
    
    
class Project(TimeStamp):    
    name = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class ProjectMember(TimeStamp):
    ROLES = ("Amin", 'Member')
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='members',
        on_delete=models.CASCADE
    )
    role = models.CharField(choices=list(zip(ROLES, ROLES)), max_length=6)
    
    def __str__(self):
        return f"{self.member.full_name} is '{self.role}' for : {self.project.name} project"
    
    
class Task(models.Model):
    PRIORITY = ('Low', 'Medium', 'High')
    STATUS = ('To Do', 'In Progress', 'Done')
    
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=list(zip(STATUS, STATUS)), max_length=13)
    priority = models.CharField(choices=list(zip(PRIORITY, PRIORITY)), max_length=6)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    
class Comment(TimeStamp):
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='comments',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str(self.content)