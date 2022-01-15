from django.contrib import admin
from frexco.models import Region, Fruit

class Regions(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('id','name')

class Fruits(admin.ModelAdmin):
    list_display = ('id','name','region')
    list_display_links = ('id','name')
    search_fields = ('id','name','region')

admin.site.register(Region, Regions)
admin.site.register(Fruit, Fruits)