from django.db import models
import string
import random

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super(URL, self).save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choices(characters, k=6))
        while URL.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choices(characters, k=6))
        return short_url

    def __str__(self):
        return self.short_url
