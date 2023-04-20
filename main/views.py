from django.urls import reverse_lazy
import openai
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, DeleteView
from .languages import lang_list
from .models import Record


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
                response_code = response["choices"][0]["text"].strip()
                # Save record
                Record.objects.create(
                    user=request.user,
                    question=code,
                    response=response_code,
                    language=lang,
                )
                return JsonResponse({"status": "success", "code": response_code})
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
                response_code = response["choices"][0]["text"].strip()
                # Save record
                Record.objects.create(
                    user=request.user,
                    question=code,
                    response=response_code,
                    language=lang,
                )
                return JsonResponse({"status": "success", "code": response_code})
            except Exception as e:
                return JsonResponse({"status": "failed"})
        else:
            return render(request, "main/suggest.html")


class PastRecordsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            records = Record.objects.filter(user=request.user)
        except:
            records = ""
        context = {"records": records}
        return render(request, "main/past.html", context)


class DeleteRecordView(LoginRequiredMixin, DeleteView):
    model = Record
    template_name = "main/delete_record.html"
    success_url = reverse_lazy("past")
