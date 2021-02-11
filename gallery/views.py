from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from gallery.form import PhotoForm, InteractionForm
from gallery.models import Photo, Interaction


class GalleryList(ListView):
    """
    Class that shows all pictures of gallery
    """
    model = Photo
    # filtering to show only visible pictures
    queryset = Photo.objects.filter(visible=True)


class GalleryCreate(CreateView):
    """
    Class that uploads all pictures of gallery
    """
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(GalleryCreate, self).form_valid(form)


class GalleryDetail(DetailView):
    model = Photo


class InteractionCreate(CreateView):
    model = Interaction
    form_class = InteractionForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(InteractionCreate, self).form_valid(form)
