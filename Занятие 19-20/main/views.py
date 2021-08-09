from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseForbidden
)

from .models import Report


def hello(request):
    html = '<h3>Hello world!</h3>'
    return HttpResponse(html)


def index(request):
    return HttpResponseForbidden('сюда нельзя')


def all_reports(request):
    reports = Report.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'main/all_reports.html', context)


def report(request, report_id: int):

    try:
        report = Report.objects.get(id=report_id)
    except:
        return HttpResponseNotFound()

    context = {
        'game_title': report.game.title,
        'game_rate': report.rating,
        'game_report': report.text,
    }
    return render(request, 'main/report.html', context)
