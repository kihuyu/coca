from __future__ import unicode_literals

from django.contrib import admin
from .models import  Datacollection
import time


class DatacollectionAdmin(admin.ModelAdmin):
    field = ['auth.user.username', 'name', 'latitude', 'longitude', 'favourite_drink', 'date_of_collection']
    list_filter = ['owner', 'date_of_collection']
    actions = ['Download']
    def Download(self, request, queryset):
        import csv
        timestr = time.strftime("%y%m%d%H%M%S")
        f = open('Download' + timestr + '.csv', 'wb')
        writer = csv.writer(f)
        writer.writerow(['owner', 'name', 'latitude', 'longitude', 'favourite_drink', 'date_of_collection'])
        for row in queryset:
            writer.writerow([row.owner, row.name, row.latitude, row.longitude, row.favourite_drink, row.date_of_collection])
    Download.short_description = "Download Selected"


#class CollectorAdmin(admin.ModelAdmin):
#    field = ['collector_name']

#admin.site.register(Collector, CollectorAdmin)
admin.site.register(Datacollection, DatacollectionAdmin)
