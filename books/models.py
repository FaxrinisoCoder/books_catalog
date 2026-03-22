from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kitob nomi")
    author = models.CharField(max_length=150, verbose_name="Muallif")
    genre = models.CharField(max_length=100, verbose_name="Janr")
    description = models.TextField(verbose_name="Qisqacha izoh")
    image = models.ImageField(upload_to='books/', verbose_name="Kitob rasmi")
    is_favorite = models.BooleanField(default=False, verbose_name="Sevimli")

    def __str__(self):
        return self.title