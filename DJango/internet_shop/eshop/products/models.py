from django.db import models

CATEGORIES=(
(0,"AUTO"),
(1, 'Bikes'),
(2, 'Chips')
)
# Create your models here.
class Product(models.Model):
    name = models.CharField("Название",max_length= 30)
    price = models.FloatField()
    decgription = models.TextField()
    category=models.PositiveIntegerField(choices=CATEGORIES)

    def __repr__(self):
        return "Product({})".format(self.name)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
