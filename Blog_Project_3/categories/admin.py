from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Categorie)


class CatrgoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug']



admin.site.register(models.Categorie, CatrgoryAdmin)
