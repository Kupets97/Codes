from django.db import models


class Relation(models.Model):
    parent = models.ForeignKey(
        'search_code.Code',
        on_delete=models.CASCADE,
        verbose_name='Родитель',
        db_index=True,
        related_name='parents'
    )
    children = models.ForeignKey(
        'search_code.Code',
        on_delete=models.CASCADE,
        max_length=10,
        verbose_name='Ребёнок',
        db_index=True,
        related_name='children'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'

    def __str__(self):
        return self.all

    @property
    def all(self):
        return f' Родитель: {self.parent}, Ребёнок: {self.children}'


class Category(models.Model):
    name = models.CharField(
        unique=True,
        db_index=True,
        max_length=64,
        verbose_name='Название категории',
    )
    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Code(models.Model):
    code = models.CharField(
        max_length=10,
        verbose_name='Код',
        unique=True,
        db_index=True,
    )
    description = models.CharField(
        max_length=300,
        verbose_name='Обозначение',
        db_index=True,
    )
    category = models.ForeignKey(
        'search_code.Category',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        db_index=True,
    )
    clean_code = models.CharField(
        max_length=10,
        verbose_name='Clean Code',
        unique=True,
        db_index=True,
        null=True,  
        blank=True, 
    )
    class Meta:
        ordering = ('id',)
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'

    def __str__(self):
        return self.all

    @property
    def all(self):
        return f' Код: {self.code}, Обозначение: {self.description}'

    def save(self, *args, **kwargs):
        self.clean_code = self.code.replace(' ', '').replace('.', '') 
        super(Code, self).save(*args, **kwargs)

    def update_clean_code(self):
        clean_code = self.code.replace(' ', '').replace('.', '')
        i = 1
        while Code.objects.filter(clean_code=clean_code).exclude(id=self.id).exists():
            clean_code = f"{clean_code}_{i}"
            i += 1
        self.clean_code = clean_code