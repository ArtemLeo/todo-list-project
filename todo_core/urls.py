from django.urls import path

from todo_core.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="todo_list"),
]

app_name = "todo_core"
