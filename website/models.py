from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_hour(value):
    if not 0 <= value <= 12:
        raise ValidationError("Hour must be between 0 and 12.")


DAY_CHOICES = (
    ("الاثنين", "الاثنين"),
    ("الثلاثاء", "الثلاثاء"),
    ("الاربع", "الاربع"),
    ("الخميس", "الخميس"),
    ("الجمعة", "الجمعة"),
    ("السبت", "السبت"),
    ("الحد", "الحد"),
)
CLASS_CHOICES = (
    ("ابتدائي", "ابتدائي"),
    ("اعدادي", "اعدادي"),
    ("ثانوي", "ثانوي"),
)


class Train(models.Model):
    instructor = models.CharField("اسم المدرب", max_length=200)
    coures_name = models.CharField("اسم الكورس", max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    days = MultiSelectField("الايام", choices=DAY_CHOICES, max_choices=7, max_length=56)

    details = models.CharField(
        "تفاصيل ",
        max_length=2000,
        blank=True,
        null=True,
        default="لا يوجد تفاصيل اخري ",
    )
    hour = models.DecimalField(
        "المعاد",
        max_digits=5,
        decimal_places=2,
        validators=[validate_hour, MinValueValidator(0), MaxValueValidator(12)],
    )

    def __str__(self) -> str:
        return f"{self.coures_name} "

    class Meta:
        verbose_name = "تدريب"
        verbose_name_plural = "تدريب"


class Coures(models.Model):
    instructor = models.CharField("اسم المدرس", max_length=200)
    coures_name = models.CharField("اسم المادة", max_length=300)
    class_type = models.CharField("المرحلة", max_length=50, choices=CLASS_CHOICES)
    class_number = models.PositiveIntegerField("السنة")
    price = models.DecimalField("السعر", max_digits=5, decimal_places=2)
    days = MultiSelectField("الايام", choices=DAY_CHOICES, max_choices=7, max_length=56)
    details = models.CharField(
        "تفاصيل ",
        max_length=2000,
        blank=True,
        null=True,
        default="لا يوجد تفاصيل اخري ",
    )
    hour = models.DecimalField(
        "المعاد",
        max_digits=5,
        decimal_places=2,
        validators=[validate_hour, MinValueValidator(0), MaxValueValidator(12)],
    )

    def __str__(self) -> str:
        return f"{self.coures_name}"

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = " درس"
