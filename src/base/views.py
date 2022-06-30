from . import csrtools
from .forms import CSRForm
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base/home.html')

def form(request):
    context = {'form'}
    return render(request,'base/forms.html', context)

def generate_csr(request):
    if request.method == 'POST':
        form = CSRForm(request.POST)

        if not form.is_valid():
            raise Exception

        csr = csrtools.CSR(
            form.cleaned_data['common_name'],
            form.cleaned_data['country'],
            form.cleaned_data['state'],
            form.cleaned_data['localty'],
            form.cleaned_data['organization'],
            form.cleaned_data['organizational_unit'],
            form.cleaned_data['key_size']
        )

        context = {'pkey': csr.private_key.rstrip(), 'csr': csr.request.rstrip()} 
        return render(request, 'base/success.html', context)
    else:
        form = CSRForm()
        context = {'form': form}

    return render(request, 'base/generate-csr.html', context)

def decode_csr(request):    
    if request.method == 'POST':
        page = 'result'
        csr = request.POST.get('csr')
        result = csrtools.decode_csr(csr)
        
        if not result:
            return HttpResponse('Error occurred. It might be an invalid CSR format.')

        context = { 'result': result, 'page': page }
        return render(request, 'base/decode-csr.html', context)

    return render(request, 'base/decode-csr.html')

def verifySSL(request):
    return render(request, 'base/verify-ssl.html')
