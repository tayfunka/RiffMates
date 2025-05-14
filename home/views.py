from django.http import HttpResponse
from django.http import JsonResponse


def credits(request):
    content = 'Nicky\nTayfun'
    return HttpResponse(content, content_type='text/plain')


def about(request):
    content = '<h1>About RiffMates</h1><p>RiffMates is a web application that helps musicians find and connect with other musicians to collaborate on music projects.</p>'
    response = HttpResponse(content, content_type='text/html')
    return response


def version(request):
    data = 'Version 1.0.0'
    response = JsonResponse({'version': data},
                            content_type='application/json')

    return response
