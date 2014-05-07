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
from pacman.models import Repository
from pacman.control import enable as enable_repos

def firststart(request):

    # hostname
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

    # repositories
    f = open('/etc/pacman.d/mirrorlist', 'r')
    content = f.read().splitlines()
    f.close()

    for l in content:
        print(l)

    for l in content:
        if re.match('^Server', l):
            url = l.split()[2]
            name = url
            isActive = True
            if not Repository.objects.filter(name=url):
                rep = Repository()
                rep.name = name
                rep.repourl = url
                rep.isActive = isActive
                rep.save()

    return HttpResponse("done")
