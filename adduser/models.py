from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    fname = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images", blank=True)
    school = models.CharField(max_length=500)
    neighborhood = models.CharField(max_length=3000)
    JSHSHIR = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    userdate = models.DateField(auto_now_add=True)
    lang = {
        ("english", "english"),
        ("others", "others"),
        ("nemesis", "nemesis"),
    }
    title = models.CharField(max_length=300, verbose_name="Language", choices=lang)
    STATUS_CHOICES = (
        ("uqimoqda", "uqimoqda"),
        ("tugatgan", "tugatgan"),
    )
    status = models.CharField(max_length=300, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    user_info = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="certificates"
    )
    lang = {
        ("english", "english"),
        ("others", "others"),
        ("nemesis", "nemesis"),
    }
    title = models.CharField(max_length=300, verbose_name="Language", choices=lang)
    overel = {
        ("B2", "B2"),
        ("C1", "C1"),
    }
    overel = models.CharField(max_length=2, verbose_name="Overel", choices=overel)
    url = models.CharField(max_length=300, blank=True)
    serticatedate = models.DateField(auto_now_add=True)
