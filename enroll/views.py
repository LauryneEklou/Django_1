from django.shortcuts import render, redirect, get_object_or_404
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
        stud = User.objects.all()
    else:
        fm = StudentRegistration()
        stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

def delete_data(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('addandshow')

def update_data(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = StudentRegistration(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('addandshow')
    else:
        form = StudentRegistration(instance=user)
    return render(request, 'enroll/updatestudent.html', {'form': form, 'id': id})