from django.contrib import admin
from .models import Menu, Item, Ingredient
from datetime import date


class YearList(admin.SimpleListFilter):
    title = "Year Created"

    parameter_name = 'laura'

    def lookups(self, request, model_admin):
        return (
            ('2015', '2015'),
            ('2016', '2016'),
            ('2017', '2017'),
            ('2018', '2018'),
        )

    def queryset(self, request, queryset):
            if self.value() == '2015':
                return queryset.filter(created_date__gte=date(2015, 1, 1),
                                       created_date__lte=date(2015, 12, 31))

            if self.value() == '2016':
                return queryset.filter(created_date__gte=date(2016, 1, 1),
                                       created_date__lte=date(2016, 12, 31))

            if self.value() == '2017':
                return queryset.filter(created_date__gte=date(2017, 1, 1),
                                       created_date__lte=date(2017, 12, 31))

            if self.value() == '2018':
                return queryset.filter(created_date__gte=date(2018, 1, 1),
                                       created_date__lte=date(2018, 12, 31))


class MenuAdmin(admin.ModelAdmin):
    # fields = ['season', 'items', 'created_date', 'expiration_date']
    fieldsets = (
        (None, {
            'fields': ('season', 'items', 'created_date',)
        }),
        ('Add Content', {
            'fields' : ('expiration_date',),
            'classes': ('collapse',)
        }),
    )
    search_fields = ['season', 'items']
    list_display = ['season', 'created_date']
    list_filter = ['created_date', 'expiration_date', YearList]


def setStandardTrue(modelAdmin, request, querryset):
    querryset.update(standard=True)
setStandardTrue.short_description = "Set Standard True for Selected Items"


def setStandardFalse(modelAdmin, request, querryset):
    querryset.update(standard=False)
setStandardFalse.short_description = "Set Standard False for Selected Items"


class ItemAdmin(admin.ModelAdmin):
    fields = ['chef' ,'name', 'description', 'created_date', 'standard', 'ingredients']
    search_fields = ['name', 'chef', 'description']
    list_display = ['item_name', 'created_date', 'standard', 'chef']
    list_editable = ['standard']
    list_filter = ['created_date', 'chef']

    radio_fields = {'chef': admin.HORIZONTAL}
    actions = [setStandardTrue, setStandardFalse]



admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Ingredient)
