from django.shortcuts import render
from minio_api.forms import Doucument

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = Doucument(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    return "done"