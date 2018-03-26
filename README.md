# fabric
David's collection of Fabric scripts for Pis and such

Base ideas: https://youtu.be/H2rTecSO0gk

Fabric main documentation: http://www.fabfile.org

Raspberry Pi RackStack: https://www.amazon.com/PiRacks-Raspberry-Acrylic-4-Stacker-Enclosure/dp/B077D4J3M5

# Basic Command Use

### Update the default password (as entered in the setup script)

`$ fab cmd:"echo pi:'newpassword' | chpasswd"`

Once you have changed the password, you will need to update the script you are using going forward for ssh access or it will bomb out on you.

### Update the software 

`$ fab cmd:"apt update"`
`$ fab cmd:"apt dist-upgrade -y"`

### Expand the root file system

`$ fab cmd:"raspi-config --expand-rootfs"`

### Reboot

`$ fab cmd"reboot now"`

