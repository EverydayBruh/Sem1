from django.db import models
# Создаем здесь нашу модель.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name
