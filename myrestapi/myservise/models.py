from django.db import models


class Books(models.Model):
    """
    Model representing a book.
    """
    name = models.CharField("Название", max_length=100)
    price = models.IntegerField("Цена", default=0)
    author = models.CharField("Автор", max_length=100)
    published = models.DateField("Дата публикации")
    category = models.CharField("Категория книги", max_length=100)
    in_stock = models.BooleanField("В наличии", default=True)
    created_at = models.DateTimeField("Дата создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения записи", auto_now=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
