from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import BugReportForm, FeatureRequestForm
from .models import BugReport, FeatureRequest


def index(request):
    return render(request, "quality_control/index.html")


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, "quality_control/bug_list.html", {"bug_list": bugs})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(
        request, "quality_control/feature_list.html", {"feature_list": features}
    )


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, "quality_control/bug_detail.html", {"bug": bug})


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, "quality_control/feature_detail.html", {"feature": feature})


def add_bug_report(request):
    if request.method == "POST":
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quality_control:bug_list")
    else:
        form = BugReportForm()
    return render(request, "quality_control/bug_report_form.html", {"form": form})


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == "POST":
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect("quality_control:bug_detail", bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(
        request, "quality_control/bug_update.html", {"form": form, "bug": bug}
    )


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect("quality_control:bug_list")


def add_feature_request(request):
    if request.method == "POST":
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quality_control:feature_list")
    else:
        form = FeatureRequestForm()
    return render(request, "quality_control/feature_request_form.html", {"form": form})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == "POST":
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect("quality_control:feature_detail", feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(
        request, "quality_control/feature_update.html", {"form": form, "bug": feature}
    )


def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect("quality_control:feature_list")


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "quality_control/index.html")


class BugListView(ListView):
    model = BugReport
    template_name = "quality_control/bug_list.html"


class FeatureListView(ListView):
    model = FeatureRequest
    template_name = "quality_control/feature_list.html"


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = "bug_id"
    template_name = "quality_control/bug_detail.html"


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = "feature_id"
    template_name = "quality_control/feature_detail.html"


def add_bug_report(request):
    if request.method == "POST":
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quality_control:bug_list")
    else:
        form = BugReportForm()
    return render(request, "quality_control/bug_report_form.html", {"form": form})
