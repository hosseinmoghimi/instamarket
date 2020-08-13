from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _
class Link(models.Model):
    title=models.CharField(_("title"), max_length=50)
    

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Link_detail", kwargs={"pk": self.pk})
