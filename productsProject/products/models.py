from django.db import models


# Model representing a product category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model representing a product tag
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model representing a product
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )  # Foreign key relationship to Category
    tags = models.ManyToManyField(Tag)  # Many-to-many relationship with Tag
    image = models.ImageField()  # Field to store product image

    def __str__(self):
        return self.name
