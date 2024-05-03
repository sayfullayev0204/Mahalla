from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Viloyat(models.Model):
    name = models.CharField(max_length=300)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "viloyat"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="viloyat_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Tuman(models.Model):
    name = models.CharField(max_length=300)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="tuman_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Mahalla(models.Model):
    name = models.CharField(max_length=300)
    tuman = models.ForeignKey("Tuman", on_delete=models.CASCADE)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahallalar"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="mahalla_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Maktab(models.Model):
    name = models.CharField(max_length=300)
    tuman = models.ForeignKey("Tuman", on_delete=models.CASCADE, default=1)
    mahalla = models.ForeignKey("Mahalla", on_delete=models.CASCADE)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="maktab_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class User(AbstractUser):
    ROLE_ADMIN = 7
    ROLE_HOKIM = 6
    ROLE_HOKIM_YORDAMCHISI = 5
    ROLE_TUMAN_MASUL = 4
    ROLE_TUMAN_YOSHLAR_ISHLARI = 3
    ROLE_MAHALLA_MASUL = 2
    ROLE_MAKTAB_MASUL = 1

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_HOKIM, "Viloyat Hokimi"),
        (ROLE_HOKIM_YORDAMCHISI, "Viloyat Hokimi Yordamchisi"),
        (ROLE_TUMAN_MASUL, "Tuman Hokimi"),
        (ROLE_TUMAN_YOSHLAR_ISHLARI, "Tuman Yoshlar Ishlari Agentligi"),
        (ROLE_MAHALLA_MASUL, "Mahalla Yoshlar Yshlari Agentligi"),
        (ROLE_MAKTAB_MASUL, "Maktabdagi mas'ul shaxs"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    tuman = models.ForeignKey(
        Tuman, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    role = models.IntegerField(choices=ROLE_CHOICES, default=ROLE_MAHALLA_MASUL)
    rank = models.IntegerField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ["role", "username"]

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="Specific permissions for this user.",
    )

    # def save(self, *args, **kwargs):
    #     if self.role == self.ROLE_ADMIN:
    #         self.rank = 4
    #     elif self.role in [self.ROLE_HOKIM, self.ROLE_HOKIM_YORDAMCHISI]:
    #         self.rank = 3
    #     elif self.role in [self.ROLE_TUMAN_MASUL, self.ROLE_TUMAN_YOSHLAR_ISHLARI]:
    #         self.rank = 2
    #     elif self.role in [self.ROLE_MAHALLA_MASUL, self.ROLE_MAKTAB_MASUL]:
    #         self.rank = 1
    #     else:
    #         raise ValueError(f"Unknown role: {self.role}")
    #     super().save(self.rank, *args, **kwargs)
