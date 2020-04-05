KASA WIFI PLUG PYTHON 3
=====
This is a script to send or receive commands from your KASA WIFI PLUG.
Just follow the instructions below to setup your script.

Installing
----------
First of all make sure you download KASA for your Mobile Device and connect the device to your Network
Once you have added your device to your network open the script folder and start typing commands.
chmod u+x main.py if permissions are missing

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



