from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll_number']
            email = form.cleaned_data['email']

            return render(request, 'students/success.html', {
                'name': name,
                'roll': roll,
                'email': email
            })
    else:
        form = StudentForm()

    return render(request, 'students/form.html', {'form': form})