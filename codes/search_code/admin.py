from django.contrib import admin
from .models import Relation, Category, Code

class RelationAdmin(admin.ModelAdmin):
    show_change_link = True

admin.site.register(Code)
admin.site.register(Relation)
admin.site.register(Category)
