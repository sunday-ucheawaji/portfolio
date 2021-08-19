from django.db import models


class Courses(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary