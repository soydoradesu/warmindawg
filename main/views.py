from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'BepeShop',
        'student_name': 'Valentino',
        'class_name': 'Kelas E-commerce'
    }
    return render(request, 'main/home.html', context)