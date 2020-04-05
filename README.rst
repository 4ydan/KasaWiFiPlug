KASA WIFI PLUG PYTHON 3
=====
This is a script to send or receive commands from your KASA WIFI PLUG.
Just follow the instructions below to setup your script.

Installing
----------
First of all make sure you have downloaded "KASA" on your mobile device and the plug is connected with your network.
If so, open the script folder and start sending commands.

.. code-block:: text

chmod u+x main.py if you are missing permissions.

A Simple Example
----------------

.. code-block:: text

    ./kasa.py -t <ip> [-c <cmd> || -j <json>]

    ./mykasa.py -t 192.168.1.177 -j {"system":{"set_relay_state":{"state":1}}}

    ./mykasa.py -t 192.168.1.177 -c 'on'

HAVE FUN

Links
-----
https://www.beardmonkey.eu/tplink/hs110/2017/11/21/collect-and-store-realtime-data-from-the-tp-link-hs110.html
https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/



