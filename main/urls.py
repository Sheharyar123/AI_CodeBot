from django.urls import path

from .views import HomePageView, SuggestView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("suggest/", SuggestView.as_view(), name="suggest"),
]
