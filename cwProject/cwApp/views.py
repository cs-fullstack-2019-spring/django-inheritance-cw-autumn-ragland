from django.shortcuts import render, redirect
from .forms import ContactForm, ContactModel

# home page (make it the CodeCrew logo clickable), About Us, Gallery with 4 pictures, Resources and Contact Us.

def index(request):
    return render(request, 'cwApp/index.html')


def about(request):
    return render(request, 'cwApp/about.html')


def gallery(request):
    return render(request, 'cwApp/gallery.html')


def resources(request):
    return render(request, 'cwApp/resources.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'cwApp/contact.html', context)


def contact_info(request):
    contact_list = ContactModel.objects.all()
    context = {
        'contact_list': contact_list
    }
    return render(request, 'cwApp/contact_info.html', context)
