#render htmls
from django.http import HttpResponse
from django.shortcuts import render # render will do the job for httpresponse
from django.template.loader import get_template

def home_page(request): #requesting a page, our view gives the request
    my_title = 'Henlo therem...'
    context = {'title': my_title}
    if request.user.is_authenticated:
        context = {'title': my_title, 'my_list':[1,2,3,4,5]}
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html', {'title':'about us'})

def contact_page(request):
    return render(request, 'hello_world.html', {'title':'Contact Us'})

def example_page(request):
    context       = {'title':'Example'}
    template_name = 'hello_world.html'
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)