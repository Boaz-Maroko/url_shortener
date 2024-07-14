from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return f"the original url is {self.original_url} and the short url is {self.short_url}"
