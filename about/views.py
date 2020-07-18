from django.shortcuts import render


def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about/about.html', context)
