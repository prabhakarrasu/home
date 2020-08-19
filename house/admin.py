from django.contrib import admin

from .models import Building, House, Teneant,Rent,WaterBill,Maintenance

admin.site.register(Building)
admin.site.register(House)
admin.site.register(Teneant)
admin.site.register(Rent)
admin.site.register(WaterBill)
admin.site.register(Maintenance)


