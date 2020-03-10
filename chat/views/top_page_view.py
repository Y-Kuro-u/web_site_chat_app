from chat.views import lobby_view

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def top_page_view(request):
    if request.method == "POST":
        return lobby_view(request)

    return render(request, "toppage/top_page.html")