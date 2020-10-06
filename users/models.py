from django.db import models
from django.urls import reverse

class User(models.Model):
    user_name = models.CharField(max_length=255)

    user_course = models.CharField(max_length=255, null=True, blank=True)

    user_primary_language = models.CharField(max_length=255)
    user_secondary_language = models.CharField(max_length=255, null=True, blank=True)

    user_preferred_time =  models.IntegerField()
    user_preferred_day = models.IntegerField()

    user_preferred_location = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('users:user_edit', kwargs={'pk': self.pk})