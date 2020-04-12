from django.shortcuts import render
from .forms import DetailsForm
from django.contrib import messages

# Create your views here.
def studentFormView(request):

    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submission Successfull')
        else:
            messages.error(request, 'There are errors in the form please check')
    else: 
        form = DetailsForm()

    context = {
        'form': form
    }
    return render(request, 'studentForm.html',context)