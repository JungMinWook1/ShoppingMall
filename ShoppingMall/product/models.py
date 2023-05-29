from django.db import models

# Create your models here.

class Category(models.Model):
    CA = models.CharField(max_length=64, verbose_name='카테고리',null=True, default='')

    def __str__(self):
        return self.CA

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품내용')
    stuck = models.IntegerField(verbose_name='재고')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name