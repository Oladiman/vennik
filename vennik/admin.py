from django.contrib import admin
from vennik.models import UserProfile,Location

# Register your models here.
admin.site.site_header='Venik Administration'
admin.site.index_title = 'Venik Administration'
admin.site.register(UserProfile)
admin.site.register(Location)