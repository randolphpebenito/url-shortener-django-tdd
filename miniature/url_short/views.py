from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render 
from .forms import URLShortenForm 
from .models import Link
from .shortener import shorten 

def home(request):
    form = URLShortenForm(request.POST or None)
    context    = {
        'form': form,
    }
    if form.is_valid():
        url = form.cleaned_data.get("url")
        su  = shorten(url)
        return redirect('url_shorten', pk=su.id)

    return render(request, 'index.html', context)

def show_url_shorten(request,pk): 
    try:
        ln = Link.objects.get(pk=pk)
    except:
        #FIX ME: Create own error html file
        raise Http404("URL does not exists")

    context    = {
        'url': ln.url,
        'redirect_url': ln.short_url,
        'short_url': '/'.join([request.META['HTTP_HOST'], ln.short_url])
    }
    return render(request, 'show_url_shorten.html', context)

def redirect_url_shorten(request, urlshort): 
    try:
        ln = Link.objects.get(short_url=urlshort)
    except:
        raise Http404("URL does not exists")

    return redirect(ln.url)
