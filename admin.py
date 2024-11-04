from django.contrib import admin
from .models import deardiaryModel, Profile, categorymodel , ReviewRating, requestcat

class categoryAdmin(admin.ModelAdmin):
	list_display=('name',) 
	search_fields=('name',)

admin.site.register(deardiaryModel)
admin.site.register(Profile)
admin.site.register(categorymodel,categoryAdmin)
admin.site.register(ReviewRating)
admin.site.register(requestcat)

