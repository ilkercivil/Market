from django.shortcuts import render,redirect

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name='index.html'

class AboutsView(TemplateView):
    template_name='abouts.html'

class ServicesView(TemplateView):
    template_name='services.html'

class BlogsView(TemplateView):
    template_name='blogs.html'

class ContactsView(TemplateView):
    template_name='contacts.html'



    

