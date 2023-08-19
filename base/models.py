from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, default="")
    sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.price}$"

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    def get_buy_url(self):
        return reverse("buy_product", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("edit_product", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("delete_product", kwargs={"pk": self.pk})
