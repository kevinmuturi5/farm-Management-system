from django.contrib import admin

from .models import Listing,ListingRecord,Labourer

class LabourerInline(admin.TabularInline):
    model = Labourer
    extra = 0
class ListingAdmin(admin.ModelAdmin):
  list_display=('name','planted_date',)
  list_per_page = 25
  prepopulated_fields = {"slug":("name",)}
  inlines = [LabourerInline]

class ListingRecordAdmin(admin.ModelAdmin):
    list_display = ('category','title',)
    prepopulated_fields = {"slug": ('title',)}  

class LabouresAdmin(admin.ModelAdmin):
    list_display = ('name', 'projects')
    search_fields = ('name', )
   

admin.site.register(Labourer, LabouresAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingRecord,ListingRecordAdmin)
