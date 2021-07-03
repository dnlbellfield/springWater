from django.shortcuts import render

# Create your views here.
def index (request):
  return render(request, 'spring_water_app/index.html', {}) 