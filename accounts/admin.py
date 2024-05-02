from django.contrib import admin
from .models import Tuman, User, Mahalla, Maktab


class TumanAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(Tuman, TumanAdmin)


class MahallaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(Mahalla, MahallaAdmin)


class MaktabAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(Maktab, MaktabAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "rank",
        "tuman",
        "last_login",
    )
    list_filter = ("role", "tuman")
    search_fields = ("username", "first_name", "last_name")
    ordering = ("role", "username")


admin.site.register(User, UserAdmin)
