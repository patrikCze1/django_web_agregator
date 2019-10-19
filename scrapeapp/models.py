from django.db import models

class Page(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name