from django.shortcuts import render
from django.views.generic import View
from .languages import lang_list


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {"lang_list": lang_list}
        return render(request, "main/index.html", context)
