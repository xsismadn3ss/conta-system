from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'partidas_index.html', status=200)