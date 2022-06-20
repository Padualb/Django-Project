from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context="")


def recipe(request, id):
    return render(request, 'recipes/pages/place-view.html', context={
        'detail_page': True
    })
