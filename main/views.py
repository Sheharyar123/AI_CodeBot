from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from .languages import lang_list


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {"lang_list": lang_list}
        return render(request, "main/index.html", context)

    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        lang = request.POST.get("lang")

        if lang == "Select Programming Language":
            messages.warning(request, "You forgot to select a language")

        context = {"code": code, "lang_list": lang_list}

        return render(request, "main/index.html", context)
