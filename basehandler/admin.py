from django.contrib import admin
from basehandler.models import Company, Parameter, IntervalData
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name','weightage')
    search_fields = ('name',)


class IntervalDataAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(IntervalData, IntervalDataAdmin)
