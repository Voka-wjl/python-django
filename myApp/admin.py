from django.contrib import admin

# Register your models here.
from .models import Grades,Students
class GradesAdmin(admin.ModelAdmin):
    list_display=['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter=['gname']
#注册
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students)
