from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date, timedelta


def credits(request):
    content = '''<a href="{% url 'credits' %}">Credits Page</a>'''
    return HttpResponse(content, content_type='text/html')


def about(request):
    content = '<h1>About RiffMates</h1><p>RiffMates is a web application that helps musicians find and connect with other musicians to collaborate on music projects.</p>'
    response = HttpResponse(content, content_type='text/html')
    return response


def version(request):
    data = 'Version 1.0.0'
    response = JsonResponse({'version': data},
                            content_type='application/json')

    return response


def news(request):
    data = {
        'news':
            [
                "RiffMates now has a news page!",
                "RiffMates has its first web page",
            ],
    }
    return render(request, 'exercise_news2.html', data)


def news_advanced(request):
    today = date.today()
    before1 = today - timedelta(days=1)
    before2 = today - timedelta(days=2)
    before3 = today - timedelta(days=3)

    data = {
        'news': [
            ("RiffMates now has a news page!", today),
            ("RiffMates has its first web page", before1),
            ("RiffMates is now open source!", before2),
            ("RiffMates has a new feature: user profiles!", before3),
        ],
    }
    return render(request, 'news_adv.html', data)
