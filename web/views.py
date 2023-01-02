from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def pajak(request):

    return render(request, 'pajak.html')

def TenagaAhli(request):

    return render(request, 'Tenaga Ahli.html')

def UMKMpribadi(request):

    return render(request, 'UMKM Pribadi.html')

def BadanUsaha(request):

    return render(request, 'Badan Usaha.html')

def error_404(request, exception):
    return render(request, '404.html')