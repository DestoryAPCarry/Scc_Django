from django.contrib import admin
from scc.models import  User_Infomation,uhome_admin,skill_admin

# Register your models here.

#======================== 博客 ===================================
class PageAdmin(admin.ModelAdmin):
    list_display = ('name','time','email')

#=====================user===========================
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email')
#===================xx================
class skilla(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(User_Infomation,UserAdmin)
admin.site.register(uhome_admin,PageAdmin)
admin.site.register(skill_admin,skilla)
