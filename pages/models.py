from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    body = RichTextField(verbose_name="Cuerpo")
    image = models.ImageField(upload_to='pages_images/', null=True, blank=True, verbose_name="Imagen")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    def __str__(self):
        return self.title
