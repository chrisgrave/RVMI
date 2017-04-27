from django.contrib import admin

# Register your models here.
from .models import Virtual_Machine

class Virtual_Machine_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Infra', 'Function', 'Business_Owner', 'Email', 'Faculty', 'Contribution', 'Nominated_Admins', 'Isilon', 'Sensitive_Data', 'Type', 'OS', 'CPUcores', 'Memory', 'HDD', 'DNS', 'IP_Address', 'Sysadmin1', 'Sysadmin2', 'Reference', 'Notes' )

admin.site.register(Virtual_Machine, Virtual_Machine_Admin)