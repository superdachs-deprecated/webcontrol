from pacman.models import Repository
from subprocess import call

def enable():
    call(['rm', '/etc/pacman.d/mirrorlist'])
    f = open('/etc/pacman.d/mirrorlist', 'w')
    for rep in Repository.objects.all():
        if rep.isActive:
            f.write('Server = ' + rep.repourl + '\n')
    f.close()

def update():
    call(['pacman', '-Sy', '--noconfirm'])

def upgrade():
    call(['pacman', '-Su', '--noconfirm'])
