from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, "upload/upload.html", context)