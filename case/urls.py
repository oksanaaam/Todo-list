from django.urls import path
from case.views import (
    index,
    TagListView,
    TagDetailView,
    TaskListView,
    TaskDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail-list"
    ),
]

app_name = "case"
