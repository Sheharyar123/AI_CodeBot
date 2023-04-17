import openai
from django.contrib import messages
from django.conf import settings
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
            print(lang)
            messages.warning(request, "You forgot to select a language")

        else:
            openai.api_key = settings.API_KEY
            # # Create OpenAI Instance
            # openai.Model.list()
            try:
                # Call the API
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"Respond only with code. Fix this {lang.lower()} code: { code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                code = response["choices"][0]["text"].strip()
                print(code)
            except Exception as e:
                print(e)

        context = {"code": code, "lang": lang, "lang_list": lang_list}

        return render(request, "main/index.html", context)
