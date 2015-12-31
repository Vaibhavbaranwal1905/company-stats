from django.contrib import admin
from utility.models import FileUpload
from utility.csv_handler import csv_handler
# Register your models here.


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('interval','data_file', 'status')
    search_fields = ('interval',)
    readonly_fields = ('status',)
    actions = [csv_handler]

csv_handler.short_description = 'Upload Data'


admin.site.register(FileUpload, FileUploadAdmin)
