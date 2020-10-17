from django.contrib import admin

from .models import Listing,ListingRecord,RecordsCartegory

class ListingAdmin(admin.ModelAdmin):
 
  list_per_page = 25
  prepopulated_fields = {"slug":("name",)}

class ListingRecordAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ('title',)}  

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingRecord,ListingRecordAdmin)
