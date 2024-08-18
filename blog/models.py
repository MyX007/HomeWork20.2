
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    preview_img = models.ImageField(upload_to='posts/', verbose_name="Превью", **NULLABLE)
    content = models.TextField(verbose_name="Содержимое")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.CharField(max_length=50, verbose_name="Автор")
    slug = models.TextField(max_length=150, verbose_name="slug", **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
