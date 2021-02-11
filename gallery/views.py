from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from gallery.form import PhotoForm, InteractionForm
from gallery.models import Photo, Interaction


class GalleryList(ListView):
    """
    Class that shows all pictures of gallery
    """
    model = Photo

    def get_queryset(self):
        return Photo.objects.filter() if self.request.user.profile.allowed_to_upload else Photo.objects.filter(visible=True)


class GalleryCreate(CreateView):
    """
    Class that uploads all pictures of gallery
    """
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        f = form.save(commit=False)
        f.owner = self.request.user.profile
        form.save()
        return super(GalleryCreate, self).form_valid(form)


class GalleryUpdate(UpdateView):
    model = Photo
    fields = ('visible', )


class GalleryDetail(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        """
        this method retrieves the comments related to the current photo
        :param kwargs:
        :return: data updated with comments
        """
        data = super().get_context_data(**kwargs)
        comments = Interaction.objects.filter(photo=self.get_object()).order_by('-created_at')
        comments = Photo.get_comments(self.get_object())
        data['interactions'] = comments
        if self.request.user.is_authenticated:
            data['comment_form'] = InteractionForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Interaction(content=request.POST.get('content'),
                                  user=self.request.user.profile,
                                  photo=self.get_object())
        new_comment.save()
        self.get_context_data()
        return self.get(self, request, *args, **kwargs)


class GalleryDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('gallery:list')
