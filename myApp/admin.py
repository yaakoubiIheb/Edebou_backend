from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User 
from .models import Item,Image,Report
from .models import User as uss



class ReportAdmin(admin.ModelAdmin):

    list_filter=['state']


admin.site.register(uss)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Report,ReportAdmin)







admin.site.site_header = "Administration"
admin.site.site_title = "Administration"
admin.site.index_title = "Administration"
admin.site.site_url=None





admin.site.unregister(Group)