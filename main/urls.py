from django.urls import path

from .views import HomePageView, SuggestView, PastRecordsView, DeleteRecordView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("suggest/", SuggestView.as_view(), name="suggest"),
    path("past/", PastRecordsView.as_view(), name="past"),
    path("delete_record/<int:pk>/", DeleteRecordView.as_view(), name="delete"),
]
