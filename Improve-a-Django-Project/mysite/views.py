from django.shortcuts import render

# Done
def home(request):
    return render(request, 'home.html')