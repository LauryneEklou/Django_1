from django.shortcuts import render
from django.contrib.auth.models import User
from .form import StudentRegistration

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)
            user.set_password(fm.cleaned_data['password'])
            user.save()
            print("User saved successfully")
        else:
            print("Form is not valid")
            print(fm.errors)
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {'form': fm})