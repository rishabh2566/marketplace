from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display= ('id','title','is_published', 'price')
    list_display_links= ('id', 'title')
    list_filter= ('realtor',)
    list_editable= ('is_published',)
admin.site.register(Listing, ListingAdmin)


