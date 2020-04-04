FIRST:
    Make sure you download the App and connect your Wifi Plug with your Device.
    Only afterwards the socket can be adressed!


THEN:
open console and type ./kasa.py -t <ip> [-c <cmd> || -j <json>]
    choose between dictionary command or json command(look inside commands.txt)
chmod u+x main.py if permissions are missing

Example:
    ./mykasa.py -t 192.168.1.177 -j {"system":{"set_relay_state":{"state":1}}}
OR
    ./mykasa.py -t 192.168.1.177 -c 'on'


HAVE FUN



