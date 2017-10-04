from django.contrib import admin
from truck_collection.models import Companies

# Set up slug creation.
class CompaniesAdmin(admin.ModelAdmin):
	model = Companies
	list_display = ('name','description')
	prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Companies, CompaniesAdmin)