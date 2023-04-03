from urllib.request import Request

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from case.models import Tag, Task


def index(request: Request) -> HttpResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1
    }

    return render(request, "case/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "case/tag_form.html"
    success_url = reverse_lazy("case:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "case/tag_form.html"
    success_url = reverse_lazy("case:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "case/tag_confirm_delete.html"
    success_url = reverse_lazy("case:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("case:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("case:task-list")


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("tags__tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("case:task-list")


def change_task(request: Request, pk: int):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("case:task-list"))
