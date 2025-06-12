from django.shortcuts import render, redirect
from enroll.forms import EnrollmentForm
from django.contrib import messages

def enroll_now(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, request.FILES)
        if form.is_valid():
            enrollment = form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('enroll_success')
    else:
        form = EnrollmentForm()
    
    return render(request, 'apply.html', {'form': form})

def enroll_success(request):
    return render(request, 'success.html')