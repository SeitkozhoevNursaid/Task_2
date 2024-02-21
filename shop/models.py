from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название категории')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название товара')
    code = models.IntegerField(verbose_name = 'Код товара')
    description = models.CharField(max_length=50, verbose_name = 'Описание товара')
    price = models.IntegerField(verbose_name = 'Цена товара')
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE, related_name = 'user')
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete = models.CASCADE, related_name = 'cat')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_number = models.IntegerField(verbose_name = 'Номер заказа', unique = True)
    user = models.ForeignKey(User, verbose_name= "Клиент", on_delete=models.CASCADE, related_name = 'order_client')
    order_product = models.ManyToManyField(Product, verbose_name = "Заказ", related_name = 'order_product')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
class Title(models.Model):
    login_user = 'LU'
    user = 'UR'
    saler = 'SL'
    admin = 'AM'
    title_choices = {
        login_user: 'login',
        user: 'user',
        saler: 'saler',
        admin: 'admin',
    }
    name_of_title = models.CharField(max_length = 10,choices = title_choices, verbose_name = 'Тип пользователя')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    
    class Meta:
        verbose_name = 'Права'
        verbose_name_plural = 'Права'
        
    def __str__(self):
        return self.name_of_title
    
