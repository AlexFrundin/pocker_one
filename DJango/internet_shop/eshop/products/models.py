from django.db import models
from django.db.models.expressions import F
from django.urls import reverse

CATEGORIES=(
(0,"AUTO"),
(1, 'Bikes'),
(2, 'Chips')
)
# Create your models here.
class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=2000)

    def set_price(self, k):
        super().get_queryset().update(price=F('price')*k)

class Product(models.Model):
    name = models.CharField("Название",max_length= 30)
    price = models.FloatField()
    decgription = models.TextField()
    category=models.PositiveIntegerField(choices=CATEGORIES)
    #без этого мой менеджер не подтянется
    objects = MyManager()

    def __repr__(self):
        return "Product({})".format(self.name)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_price(self):
        return "{} uah".format(self.price)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"product_id":self.pk})

class Feedback(models.Model):
    product= models.ForeignKey(Product)
    feedback = models.TextField('Feedback')
    nick = models.CharField('name', max_length=20)
    date= models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "Feedback {} {} ".format(self.nick, self.product)
