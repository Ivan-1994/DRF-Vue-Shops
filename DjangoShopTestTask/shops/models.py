from django.db import models
from users.models import User


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_user')
    connected_users = models.ManyToManyField(User, related_name='shop', blank=True)

    def __str__(self):
        return f'{self.shop_id}  {self.name}'
