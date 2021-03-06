from django.urls import path

from jobpostings.views import ApplyView, PostingsView, SuggestView, TagCategoryView, JobGroupView, PostingView, SalaryView

urlpatterns = [
    path("", PostingsView.as_view()),
    path("/suggested", SuggestView.as_view()),
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
    path("/<int:posting_id>", PostingView.as_view()),
    path('/<int:posting_id>/apply', ApplyView.as_view()),
    path("/salary", SalaryView.as_view()),
]