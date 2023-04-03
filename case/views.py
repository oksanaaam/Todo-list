from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

from case.models import Tag, Task


def index(request: Request) -> HttpResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }

    return render(request, "case/index.html", context=context)
