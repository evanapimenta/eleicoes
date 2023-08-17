from easy_select2 import select2_modelform

from django.contrib import admin

from registry.models import State, People, Address


class AddressInLine(admin.StackedInline):
    model = Address
    extra = 1
    form = select2_modelform(Address)
    

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    fields_filtered = filter(lambda field: field.name not in ['id', 'created_at'], People._meta.fields)
    list_display = [field.name for field in fields_filtered]
    ordering = ('name',)
    search_fields = ('name',)

    inlines = [AddressInLine]