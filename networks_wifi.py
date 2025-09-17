## This program will find available wifi networks

import subprocess

nw= subprocess.check_output(['netsh','wlan','show','network'])

decoded_networks=nw.decode('ascii')

print(decoded_networks)