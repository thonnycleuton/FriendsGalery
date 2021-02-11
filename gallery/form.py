from django import forms

from gallery.models import Photo, Interaction


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('created_at',)


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('content',)
