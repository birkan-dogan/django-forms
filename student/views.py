from django.shortcuts import render, redirect

from .models import Student

from .forms import StudentForm
# Create your views here.
def index(request):
    return render(request, "student/index.html")

# def student_page(request):
#     return render(request, "student/student.html")

def student_page(request):
    # print(request.POST)
    # print(request.FILES)
    form = StudentForm()
    if(request.method == "POST"):
        form = StudentForm(request.POST, request.FILES)
        if(form.is_valid()):
            student_data = {
                "first_name":form.cleaned_data.get("first_name"),
                "last_name":form.cleaned_data.get("last_name"),
                "number":form.cleaned_data.get("number"),
                "profile_pic":form.cleaned_data.get("profile_image")
            }
            student = Student(**student_data)  # Student.objects.create(**student_data)
            student.save()
            return redirect("index")
    context = {
        "form":form
    }
    return render(request, "student/student.html", context)