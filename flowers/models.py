from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # صاحب السلة
    product_name = models.CharField(max_length=100)           # اسم المنتج
    description = models.TextField(blank=True)                # وصف المنتج (اختياري)

    # اسم ملف الصورة فقط، ويُفترض وجودها داخل مجلد static/images/
    image = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)         # الكمية
    price = models.DecimalField(max_digits=8, decimal_places=2)  # السعر
    created_at = models.DateTimeField(auto_now_add=True)      # وقت الإضافة

    def __str__(self):
        return f"{self.product_name} × {self.quantity}"

    @property
    def total_price(self):
        return self.quantity * self.price
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

