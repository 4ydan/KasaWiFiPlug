chmod u+x main.py if permissions are missing
open console and type ./kasa.py -t <ip> [-c <cmd> || -j <json>]

Example:
    ./mykasa.py -t 192.168.1.177 -j {"system":{"set_relay_state":{"state":1}}}
OR
    ./mykasa.py -t 192.168.1.177 -c 'on'



