from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from case.models import Tag, Task


def index(request: Request) -> HttpResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }

    return render(request, "case/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagDetailView(generic.DetailView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("tags__tasks")
