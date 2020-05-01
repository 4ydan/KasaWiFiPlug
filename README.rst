KASA WIFI PLUG PYTHON 3
=====
This is a script to send or receive commands from your KASA WIFI PLUG.
Just follow the instructions below to setup your script.

Installing
----------
1. Connect your Device to your local Network with the "KASA" App
2. Modify the IP Adress in kasa.py to your devices IP Adress
3. Import kasa to your project.
3. Create an Instance of the Class Plug and start sending commands

A Available Commands
----------------
.command(info),
.command(on),
.command(off),
.command(time),
.command(reboot),
.command(energy), only available on Model HS110!


A Simple Example
----------------

.. code-block:: text
plug1 = PLug()
plug1.command(on)
plug1.command(off)
plug1.command(info)
etc
look in the commands.txt for further commands

HAVE FUN

Links
-----
https://www.beardmonkey.eu/tplink/hs110/2017/11/21/collect-and-store-realtime-data-from-the-tp-link-hs110.html
https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/



