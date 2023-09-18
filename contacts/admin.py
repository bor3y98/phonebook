from django.contrib import admin
from contacts.models import Contact, ContactPhone


class ContactPhoneInline(admin.StackedInline):
    model = ContactPhone
    extra = 0

class CareerFormAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("id", "name", "email")
    inlines = [ContactPhoneInline]


# Register your models here.
admin.site.register(Contact, CareerFormAdmin)
