from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Contact Details</h1>")
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_context = {
        "my_text": "I am Roy",
        "my_number": 6290409930,
        'my_list' : [1, 12, 123, 1234, "roy"]
    }
    return render(request, 'about.html', my_context)



def education_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Education Details</h1>")
    return render(request, 'education.html', {})



def experience_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>My Experience</h1>")
    return render(request, 'experience.html', {})


