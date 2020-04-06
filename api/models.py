from djongo import models


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()


class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog,
    )


class Receita(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Livro(models.Model):
    receitas = models.ArrayField(
        model_container=Receita
    )
