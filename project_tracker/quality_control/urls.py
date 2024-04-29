from django.urls import path
from tasks import views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bugs/", views.bug_list, name="bug_list"),
    path("features/", views.feature_list, name="feature_list"),
    path("bugs/<int:bug_id>/", views.bug_detail, name="bug_detail"),
    path("features/<int:feature_id>/", views.feature_detail, name="feature_detail"),
    path("bug/new/", views.add_bug_report, name="add_bug_report"),
    path("feature/new/", views.add_feature_request, name="add_feature_request"),
    # path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.BugListView.as_view(), name='bug_list'),
    # path('features/', views.FeatureListView.as_view(), name='feature_list'),
    # path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]
