from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from beer_recommend_prj.settings import MEDIA_ROOT
from search.models import Beer


class User(AbstractUser):
    class GenderChoices(models.IntegerChoices):
        MALE = 0, "남성"
        FEMALE = 1, "여성"

    gender = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2),
        ],
        null=True,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )

    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
        ],
        null=True,
    )

    email = models.EmailField(max_length=40, blank=True)

    bestbeer = models.CharField(max_length=40, blank=True)

    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)