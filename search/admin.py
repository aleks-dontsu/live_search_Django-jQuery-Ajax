from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post


@admin.register(Post)
class EventAdmin(admin.ModelAdmin):
    """ Посты """
    list_display = ("name", "is_active", "get_photo")
    list_display_links = ("name",)
    readonly_fields = ("get_photo",)
    list_editable = ("is_active",)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width="90" height="60">')
        else:
            return 'Фото отсутствует'

    get_photo.short_description = "Изображение"


admin.site.site_title = "Live Search"
admin.site.site_header = "Live Search"
