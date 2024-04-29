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
    path("bugs/<int:bug_id>/update/", views.update_bug, name="update_bug"),
    path("bugs/<int:bug_id>/delete/", views.delete_bug, name="delete_bug"),
    path(
        "features/<int:feature_id>/update/", views.update_feature, name="update_feature"
    ),
    path(
        "features/<int:feature_id>/delete/", views.delete_feature, name="delete_feature"
    ),
    # path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.BugListView.as_view(), name='bug_list'),
    # path('features/', views.FeatureListView.as_view(), name='feature_list'),
    # path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]
