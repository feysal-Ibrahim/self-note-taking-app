from django.shortcuts import render
from django.template import RequestContext , loader
from django.http import HttpResponse
from django.http import HttpResponse , Http404
from .models import Note
from .forms import NoteForm


# Create your views here.

def home(request):
    notes=Note.objects.all()
    form=NoteForm( request.POST or None )
    if form.is_valid( ):
        save_it=form.save( commit=False )
        save_it.save( )
    return render( request , 'note.html' , {"notes":notes,"form":form} )