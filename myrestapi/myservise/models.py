from django.db import models


class Authors(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Genres(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Books(models.Model):
    """
    Model representing a book.
    """
    name = models.CharField("Название", max_length=100)
    price = models.IntegerField("Цена", default=0)
    author = models.ForeignKey("Authors", help_text="Автор", max_length=100, on_delete=models.CASCADE, null=False)
    published = models.DateField("Дата публикации")
    category = models.ManyToManyField(Genres, help_text="Категория книги", max_length=100)
    in_stock = models.BooleanField("В наличии", default=True)
    created_at = models.DateTimeField("Дата создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения записи", auto_now=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
