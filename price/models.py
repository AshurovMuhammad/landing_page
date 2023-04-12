from django.db import models


# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name="Narxi")
    pc_description = models.CharField(max_length=200, verbose_name="Tasnifi")

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Narx'
        verbose_name_plural = 'Narxlar'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name="Xizmat ko'rsatish")
    pt_old_price = models.CharField(max_length=200, verbose_name='Eski narx')
    pt_new_price = models.CharField(max_length=200, verbose_name='Yangi narx')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = "Xizmat ko'rsatish"
        verbose_name_plural = "Xizmat ko'rsatishlar"
