from django.contrib import admin

from .models import Aquarium, PHMeasurement, AquariumImage

admin.site.register(Aquarium)
admin.site.register(PHMeasurement)
admin.site.register(AquariumImage)
