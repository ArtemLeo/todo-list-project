from django.views import generic

from todo_core.models import Task


class TaskListView(generic.ListView):
    model = Task
