from django.contrib import admin
from .models import Bb
from .models import Rubrik




class BbAdmin(admin.ModelAdmin):
	list_display = ("title", "content", "price", "rubrik", "published")
	list_display_links = ("title", "content")
	search_fields = ("title", "content")

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubrik)


# Register your models here.
