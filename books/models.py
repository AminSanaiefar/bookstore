from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    book_cover = models.ImageField(upload_to='book_covers/', blank=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
