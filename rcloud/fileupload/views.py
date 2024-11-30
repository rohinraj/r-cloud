from django.shortcuts import render, redirect
from .forms import FileForm
from .models import File

def file_upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form, which automatically saves the file and other data to the database
            form.save()

            # Redirect to success view
            return redirect('success')
    else:
        form = FileForm()
    return render(request, 'file_upload.html', {'form': form})

def upload_success_view(request):
    return render(request, 'upload_success.html')
