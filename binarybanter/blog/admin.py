from django.contrib import admin
from .models import Post, Subscription


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)