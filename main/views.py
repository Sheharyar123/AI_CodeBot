import openai
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .languages import lang_list


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        context = {"lang_list": lang_list}
        return render(request, "main/index.html", context)

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            code = request.POST.get("code")
            lang = request.POST.get("lang")

            if lang == "Select Programming Language":
                return JsonResponse({"status": "failed"})

            try:
                openai.api_key = settings.API_KEY

                # Call the API
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"Respond only with code. Fix this {lang.lower()} code: { code}",
                    temperature=0,
                    max_tokens=500,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                code = response["choices"][0]["text"].strip()
                return JsonResponse({"status": "success", "code": code})
            except Exception as e:
                return JsonResponse({"status": "failed"})
        else:
            return render(request, "main/index.html")


class SuggestView(View):
    def get(self, request, *args, **kwargs):
        context = {"lang_list": lang_list}
        return render(request, "main/suggest.html", context)

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            code = request.POST.get("code")
            lang = request.POST.get("lang")

            if lang == "Select Programming Language":
                return JsonResponse({"status": "failed"})

            try:
                openai.api_key = settings.API_KEY
                # Call the API
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"Suggest code in {lang} for {code}. Just respond with code",
                    temperature=0.5,
                    max_tokens=1500,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                print(response)
                code = response["choices"][0]["text"].strip()
                return JsonResponse({"status": "success", "code": code})
            except Exception as e:
                return JsonResponse({"status": "failed"})
        else:
            return render(request, "main/suggest.html")
