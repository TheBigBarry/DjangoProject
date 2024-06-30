from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    product_name = models.CharField('Nombre del Producto', max_length=400)
    descripcion = models.CharField('Descripcion del Producto', max_length=200)  
    precio_original = models.IntegerField('Precio Original del Producto', default=0)
    precio_actual = models.IntegerField('Precio Actual del Producto', default=0)
    stock = models.IntegerField('Stock restante del producto', default=0)
    product_id = models.AutoField('Id del producto', primary_key=True)
    product_img = models.ImageField('Imagen del producto', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.product_name


class Usuario(models.Model):
    nombre = models.CharField('Nombre de usuario', max_length=20)
    user_id = models.IntegerField('Id del usuario', primary_key=True, default='0')
    email = models.EmailField('Correo del usuario', unique=True, max_length=100, blank=True, null=True)
    password = models.CharField('Contraseña del usuario', unique=True, max_length=20)
    saldo = models.IntegerField('Saldo disponible', default=0)

    def __str__(self):
        return self.nombre