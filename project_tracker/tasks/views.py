from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import FeedbackForm, ProjectForm, TaskForm
from .models import Project, Task


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return redirect("/tasks")
    else:
        form = FeedbackForm()
    return render(request, "tasks/feedback.html", {"form": form})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:projects_list")
    else:
        form = ProjectForm()
    return render(request, "tasks/project_create.html", {"form": form})


def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("tasks:project_detail", project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(
        request, "tasks/project_update.html", {"form": form, "project": project}
    )


def update_task(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_detail", project_id=project_id, task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_update.html", {"form": form, "task": task})


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect("tasks:projects_list")


def delete_task(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("tasks:project_detail", project_id=project_id)


def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect("tasks:project_detail", project_id=project.id)
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form, "project": project})


def index(request):
    return render(request, "tasks/index.html")


def projects_list(request):
    projects = Project.objects.all()
    return render(request, "tasks/projects_list.html", {"project_list": projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "tasks/project_detail.html", {"project": project})


def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, "tasks/task_detail.html", {"task": task})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tasks/index.html")


class ProjectsListView(ListView):
    model = Project
    template_name = "tasks/projects_list.html"


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = "project_id"
    template_name = "tasks/project_detail.html"


class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = "task_id"
    template_name = "tasks/task_detail.html"
