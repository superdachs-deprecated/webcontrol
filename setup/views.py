from django.shortcuts import render
from django.http import HttpResponse
import socket
from network_base.models import Hostname, NetworkInterface, NetworkInterfaceMode
from subprocess import call
from subprocess import Popen
import subprocess
import shlex
import re

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

    mode = NetworkInterfaceMode()
    mode.mode_name = "default"
    mode.mode_description = "default nic mode"
    mode.save()

    for nic_name in nic_names:
        if not NetworkInterface.objects.filter(device = nic_name):
            interface = NetworkInterface()
            interface.device = nic_name.strip().decode('ascii')
            interface.mode = mode
            interface.interface_description = "auto generated interface from system"
            interface.ip_address = "unknown"
            interface.netmask = "unknown"
            interface.gateway = "unknown"
            interface.interface_name = interface.device
            interface.mac = "unknown"

            interface.save()

    return HttpResponse("done")

