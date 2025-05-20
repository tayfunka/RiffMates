from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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
    return render(request, 'news.html', data)
