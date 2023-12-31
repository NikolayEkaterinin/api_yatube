from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Заголовок')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    image = models.ImageField(upload_to='posts/',
                              null=True,
                              blank=True,
                              verbose_name='Изображение')
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              blank=True,
                              null=True,
                              verbose_name='Группа')

    def __str__(self):
        return f"{self.text[:50]}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Дата добавления',
                                   auto_now_add=True,
                                   db_index=True,
                                   )

    def __str__(self):
        return str(self.created)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
