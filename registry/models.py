from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _


##
class State(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=250, verbose_name="Estado"
    )
    abbreviation = models.CharField(
        null=False, blank=False, max_length=2, verbose_name="UF"
    )

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("State_detail", kwargs={"pk": self.pk})


class Address(models.Model):
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Estado",
        related_name="state",
    )
    postal_code = models.CharField(
        max_length=9, null=False, blank=False, verbose_name="CEP"
    )
    city = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Cidade"
    )
    street = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Logradouro"
    )
    number = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Número"
    )
    person_address = models.OneToOneField(
        "People", on_delete=models.CASCADE, related_name="address"
    )


class People(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=250, verbose_name="Nome"
    )
    age = models.PositiveIntegerField(null=False, blank=False, verbose_name="Idade")
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name="CPF")

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("People_detail", kwargs={"pk": self.pk})
