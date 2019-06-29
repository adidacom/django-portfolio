from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
        )
    list_display = ["__str__", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "body"]

    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)
