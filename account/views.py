from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from account.form import ProfileForm
from account.models import Profile


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('accounts:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ProfileCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    pass


class ProfileDelete(DeleteView):
    pass
