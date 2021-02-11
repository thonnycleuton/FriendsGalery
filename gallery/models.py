from django.db import models
from django.urls import reverse

from account.models import Profile


class Photo(models.Model):
    """
    This class is responsible for handle all photographs stuff
    TODO: provide a better description for this class
    """
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos', blank=True, default='no-image-box.png')
    visible = models.BooleanField(default=False)

    def get_interactions(self, status):
        """
        Gets all interactions in the current picture
        :param status:
        :return:
        """
        interactions = Interaction.objects.filter(photo=self.id, content__isnull=status).all()
        return interactions

    def get_comments(self):
        """
        Gets all comments in the current picture
        :return:
        """
        return self.get_interactions(False)

    def get_like(self):
        """
        Gets all likes in the current picture
        :return:
        """
        return self.get_interactions(True)

    def get_absolute_url(self):
        return reverse('gallery:list')


class Interaction(models.Model):
    """
    This Class models the Comment feature
    TODO: provide a better description for this class
    """

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'pk': self.photo.pk})
