from django.contrib import admin

# from .models import Event
# class EventAdmin(admin.ModelAdmin) :
#     list_display = ('title', 'content', 'start_time', 'category','published')
#     list_display_links = ('title', 'content')
#     search_fields = ('title', 'content', )
# admin.site.register (Event, EventAdmin)

from .models import Category
admin.site.register(Category)