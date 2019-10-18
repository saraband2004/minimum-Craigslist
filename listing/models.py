from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    caption = models.CharField(max_length=120)
    texts = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption


 #   def get_absolute_url(self):
 #       return reverse('listing-detail', kwargs={'pk': self.pk})

 #   def get_success_url(self):
 #       return reverse('thankyou')