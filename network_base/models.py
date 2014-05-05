from django.db import models

class NetworkInterfaceMode(models.Model):
    mode_name = models.CharField(max_length=10) #e.g. dhcp, static
    mode_description = models.TextField()

class NetworkInterface(models.Model):
    device = models.CharField(max_length=200) #e.g. /dev/eth0
    mode = models.ForeignKey(NetworkInterfaceMode)
    interface_name = models.CharField(max_length=10)
    interface_description = models.TextField()
    ip_address = models.CharField(max_length=15)
    netmask = models.CharField(max_length=15)
    gateway = models.CharField(max_length=15)
