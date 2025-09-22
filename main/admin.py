from django.contrib import admin
from .models import Talaba,Muallif,Kitob,Admin,Record
from django.contrib.auth.models import Group,User, AbstractUser

class AdminAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "ish_vaqti")
    search_fields = ("ism",)
    list_filter = ("ish_vaqti",)

class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kitob_soni", "tirik")
    search_fields = ("ism",)
    list_filter = ("tirik",)
    list_display_links = ("id", "ism")
    list_editable = ("kitob_soni", "tirik")

class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "talaba", "kitob", "admin", "olingan_sana", "qaytarish_sana")
    search_fields = ("talaba__ism", "kitob__nom", "admin__ism")

admin.site.register(Talaba)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Record, RecordAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Kutubxona Admin paneli"
admin.site.site_title = "Kutubxona boshqaruvi"
admin.site.index_title = "Kutubxona"