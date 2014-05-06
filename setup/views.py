from django.shortcuts import render
from django.http import HttpResponse
import socket
from network_base.models import Hostname, NetworkInterface, NetworkInterfaceMode
from subprocess import call
from subprocess import Popen
import subprocess
import shlex
import re
import netifaces

def firststart(request):

    # hostname
    call(["cp", "/etc/hostname", "/etc/hostname.original"])
    sys_hostname = socket.gethostname() 
    if Hostname.objects.all().count() > 0:
        hostname = Hostname.objects.all()[0]
    else:
        hostname = Hostname()
    hostname.hostname = sys_hostname
    hostname.save()

    # nics
    
    cmd = "ls /sys/class/net/"
    args = shlex.split(cmd)
    out,err = subprocess.Popen(args, stdout = subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    nic_names = out.split()

    nic_names = netifaces.interfaces()

    if not NetworkInterfaceMode.objects.filter(mode_name='static'):
        mode = NetworkInterfaceMode()
        mode.mode_name = "static"
        mode.mode_description = "static ip configuration"
        mode.save()
    if not NetworkInterfaceMode.objects.filter(mode_name='dhcp'):
        mode = NetworkInterfaceMode()
        mode.mode_name = "dhcp"
        mode.mode_description = "get ip adress from dhcp server"
        mode.save()
    
    for nic_name in nic_names:
        if nic_name == 'lo':
            continue
        if not NetworkInterface.objects.filter(device = nic_name):

            gateway = 'unknown'

            gws = netifaces.gateways()
            gw = gws['default'][netifaces.AF_INET]
            if gw[1] == nic_name:
                gateway = gw[0]
            addresses = netifaces.ifaddresses(nic_name)
            mac = addresses[netifaces.AF_LINK][0]['addr']
            try:
                ip = addresses[netifaces.AF_INET][0]['addr']
            except Exception:
                ip = 'none'
            try:
                netmask = addresses[netifaces.AF_INET][0]['netmask']
            except Exception:
                netmask = 'none'

            interface = NetworkInterface()
            interface.device = nic_name
            interface.mode = NetworkInterfaceMode.objects.filter(mode_name='dhcp')[0]
            interface.interface_description = "auto generated interface from system"
            interface.ip_address = ip
            interface.netmask = netmask
            interface.gateway = gateway
            interface.interface_name = interface.device
            interface.mac = mac
            interface.save()

    return HttpResponse("done")

