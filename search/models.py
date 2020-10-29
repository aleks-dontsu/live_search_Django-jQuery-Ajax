from django.db import models


class Post(models.Model):
    url = models.SlugField('Url', max_length=100, default='')
    title = models.CharField("Заголовок (title)", max_length=70, blank=True)
    name = models.CharField("Название", max_length=300)
    text = models.TextField("Основной текст поста", blank=True)
    photo = models.ImageField("Фото", upload_to="blog/", blank=True)
    is_active = models.BooleanField('Выложить на сайт', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "БЛОГ"
        verbose_name_plural = "БЛОГ (посты)"
