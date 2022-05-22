from django.db import models

# Create your models here.


class Country(models.Model):
    title = models.CharField("Называния страны", max_length=100)
    code = models.SmallIntegerField("Код страны")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страны"
        verbose_name_plural = "Страны"


class Position(models.Model):
    title = models.CharField(("Наименования должности"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"


class Customer(models.Model):
    fullName = models.CharField("ФИО", max_length=100)
    companyName = models.CharField("Названия компаний", max_length=100)
    country = models.ForeignKey(Country, verbose_name=(
        "Страна"), on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, verbose_name=(
        "Должность"), on_delete=models.SET_NULL, null=True)
    email = models.EmailField("Электронная почта")

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"
