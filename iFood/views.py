from django.shortcuts import render

def home(request):
    context={'title':'teste'}
    return render(request,
                   'iFood/index.html', context)
# Create your views here.
