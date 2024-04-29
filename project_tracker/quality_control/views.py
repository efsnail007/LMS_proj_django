from django.shortcuts import get_object_or_404, render

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
