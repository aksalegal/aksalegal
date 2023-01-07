from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def pajak(request):

    return render(request, 'pajak.html')

def TenagaAhli(request):

    return render(request, 'tenagaahli.html')

def UMKMpribadi(request):

    return render(request, 'umkmpribadi.html')

def BadanUsaha(request):

    return render(request, 'badanusaha.html')

def error_404(request, exception):
    return render(request, '404.html')
