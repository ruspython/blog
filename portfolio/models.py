from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    snapshot = models.ImageField(upload_to='portfolio/images')
    link = models.URLField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_snapshot_url(self):
        return self.snapshot.url
