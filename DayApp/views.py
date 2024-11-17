from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')
def team(request):
    return render(request, 'team.html')
def myservice(request):
    return render(request, 'service-details.html')
def myportfolio(request):
    return render(request, 'portfolio-details.html')