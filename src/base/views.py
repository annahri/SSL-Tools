from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CSRForm
from .csrtools import create_csr, decode_csr


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def form(request):
    context = {'form'}
    return render(request,'base/forms.html', context)

def generateCSR(request):
    if request.method == 'POST':
        form = CSRForm(request.POST)
        if form.is_valid():
            pkey, csr = create_csr(
                form.cleaned_data['common_name'],
                form.cleaned_data['country'],
                form.cleaned_data['state'],
                form.cleaned_data['localty'],
                form.cleaned_data['organization'],
                form.cleaned_data['organizational_unit'],
                form.cleaned_data['key_size']
            )
            context = {'pkey': pkey.decode('utf-8').rstrip(), 'csr': csr.decode('utf-8').rstrip()} 
            return render(request, 'base/success.html', context)
    else:
        form = CSRForm()
        context = {'form': form}

    return render(request, 'base/generate-csr.html', context)

def decodeCSR(request):    
    if request.method == 'POST':
        page = 'result'
        csr = request.POST.get('csr')
        result, err = decode_csr(csr)
        
        if err is not None:
            return HttpResponse('Error occurred. It might be an invalid CSR format.')

        context = { 'result': result, 'page': page }
        return render(request, 'base/decode-csr.html', context)

    return render(request, 'base/decode-csr.html')

def verifySSL(request):
    return render(request, 'base/verify-ssl.html')
