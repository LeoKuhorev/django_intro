from django.shortcuts import render


def welcome_page(request):
    context = {
        'title': 'Welcome!'
    }
    return render(request, 'demo_app/welcome.html', context)
