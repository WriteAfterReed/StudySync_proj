from django.db import models
from django.urls import reverse

class Group(models.Model):
    DAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
        ('N', 'Sunday')
    )

    owner_name = models.CharField(max_length=255)
    
    # owner_name = models.ForeignKey( User, models.SET_NULL, 
    #                             blank=True,
    #                             null=True,)

    group_name = models.CharField(max_length=255)
    group_course = models.CharField(max_length=255)

    group_primary_language = models.CharField(max_length=255)
    group_secondary_language = models.CharField(max_length=255, null=True, blank=True)

    meeting_time =  models.IntegerField()
    meeting_day = models.IntegerField()
    meeting_location = models.CharField(max_length=255)


    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse('groups:group_edit', kwargs={'pk': self.pk})