from django.shortcuts import render
from web.models import SolvedApplication


def main_view(request):
    solved_applications = SolvedApplication.objects.order_by('-created_at')[:4]
    return render(request, "web/main.html", context={'solved_applications': solved_applications})


def in_developing_view(request):
    return render(request, "web/in_dev.html")
