from django.db import models


# Ariza holati
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name="Xolat nomi")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Xolat"
        verbose_name_plural = "Xolatlar"


# Buyurtmalar
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan vaqti")
    order_name = models.CharField(max_length=200, verbose_name="Ism")
    order_phone = models.CharField(max_length=14, verbose_name="Telefon")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Xolati")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class CommentsCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Buyurtma")
    comment_text = models.TextField(verbose_name='Komentariya matni')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Yaratilga vaqti')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Komentariya'
        verbose_name_plural = 'Komentariyalar'
