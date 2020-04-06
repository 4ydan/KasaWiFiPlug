KASA WIFI PLUG PYTHON 3
=====
This is a script to send or receive commands from your KASA WIFI PLUG.
Just follow the instructions below to setup your script.

Installing
----------
First of all make sure you have downloaded "KASA" on your mobile device and the plug is connected with your network.
Write your device ip in "kasa.py", your default port should be 9999 and then you should be ready to go

if you are missing permissions running kasa.py dont forget to:
<chmod u+x main.py> 

A Simple Example
----------------

.. code-block:: text

    ./kasa.py [-c <cmd> || -j <json>]

    ./mykasa.py -j {"system":{"set_relay_state":{"state":1}}}

    ./mykasa.py -c 'on'

HAVE FUN

Links
-----
https://www.beardmonkey.eu/tplink/hs110/2017/11/21/collect-and-store-realtime-data-from-the-tp-link-hs110.html
https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/



