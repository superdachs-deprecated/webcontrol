from django.contrib import admin
from network_base.models import NetworkInterface
from network_base.models import NetworkInterfaceMode
from network_base.models import Hostname

admin.site.register(NetworkInterface)
admin.site.register(NetworkInterfaceMode)
admin.site.register(Hostname)
