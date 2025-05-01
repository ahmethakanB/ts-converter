from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Ürün Adı", max_length=100)
    description = models.TextField("Açıklama", blank=True)
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stok Miktarı")
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)
    is_dismantling = models.BooleanField("Sökülebilir mi", default=False)
    is_plannable = models.BooleanField("Planlanabilir mi", default=False)

    def __str__(self):
        return self.name


class OrderType(models.Model):
    name = models.CharField("Sipariş Tipi", max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField("Sipariş Adı", max_length=100)
    description = models.TextField("Açıklama", blank=True)
    start_datetime = models.DateTimeField("Başlangıç Zamanı")
    end_datetime = models.DateTimeField("Bitiş Zamanı")
    type = models.ForeignKey(OrderType, verbose_name="Sipariş Tipi", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name="Ürünler", related_name="orders")

    def __str__(self):
        return self.name