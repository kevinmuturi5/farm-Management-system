from django.contrib import admin

from .models import Listing,ListingRecord,RecordsCartegory

class ListingAdmin(admin.ModelAdmin):
 
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingRecord,)
admin.site.register(RecordsCartegory)