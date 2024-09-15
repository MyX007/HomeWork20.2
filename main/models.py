from django.db import models

from users.models import User

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")
    description = models.CharField(max_length=150, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=150, verbose_name="Описание")
    img = models.ImageField(upload_to="products_img/", verbose_name="Фото", **NULLABLE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="Категория"
    )
    price = models.PositiveIntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения", auto_now=True
    )
    seller = models.ForeignKey(User, verbose_name="Продавец", help_text="", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name="version",
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_index = models.CharField(max_length=20, verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название")
    is_actual = models.BooleanField(default=True, verbose_name="Актуальная версия")

    def __str__(self):
        return f"{self.version_name} ({self.version_index})"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
