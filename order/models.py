from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) ##
    total = models.FloatField() ##
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Approved'),
            ('C', 'Created'),
            ('R', 'Rejected'),
            ('P', 'Pending'),
            ('S', 'Sent'),
            ('F', 'Finalized'),
        )
    ) ##

    def __str__(self):
        return f'Order number {self.pk}.' ##

class OrderItem(models.Model): ##
    order = models.ForeignKey(Order, on_delete=models.CASCADE) ##
    product_name = models.CharField(max_length=255) ##
    product_id = models.PositiveBigIntegerField() ##
    variation = models.CharField(max_length=255) ##
    variation_id = models.PositiveBigIntegerField() ##
    price = models.FloatField()
    price_promotional = models.FloatField(default=0) ##
    quantity = models.PositiveBigIntegerField() ##
    image = models.CharField(max_length=2000) ##

    def __str__(self):
        return f'Order Item {self.order}.' ##
    
    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'


# https://linktr.ee/edsoncopque