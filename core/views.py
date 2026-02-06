from django.shortcuts import render

def home(request):
    # ADD 'core/' BEFORE the filename
    return render(request, 'core/index.html') 

def about(request):
    return render(request, 'core/about.html') # Do this for all views

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')

def blog(request):
    return render(request, 'core/blog.html')

def projectdetail(request):
    return render(request, 'core/project-detail.html')

def project(request):
    return render(request, 'core/project.html')

def servicedetail(request):
    return render(request, 'core/service-detail.html')

def singlepost(request):
    return render(request, 'core/single-post.html')


def team(request):
    return render(request, 'core/team.html')


def testimonial(request):
    return render(request, 'core/testimonial.html')


def forforpage(request):
    return render(request, 'core/forforpage.html')


