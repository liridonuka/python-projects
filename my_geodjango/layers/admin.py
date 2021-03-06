from django.contrib import admin
from layers.models import Religion,CityPark,AllLayers
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class ReligionAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('name', 'location')
class CityParkAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Religion,ReligionAdmin)
admin.site.register(CityPark,CityParkAdmin)
admin.site.register(AllLayers,LeafletGeoAdmin)
