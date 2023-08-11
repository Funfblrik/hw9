from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "desrciption", "price", "created_date", "updated_date", "auction", "user", "get_image"]
    list_filter = ['auction', 'created_at', 'updated_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'desrciption', "user", 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    def get_image(self, adv):
        if adv.image:
            return mark_safe(f"<img src='{adv.image.url}' width = '50' height='60'>")
    get_image.short_description = "Изображение"

admin.site.register(Advertisement, AdvertisementAdmin)
