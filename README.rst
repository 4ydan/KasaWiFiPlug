KASA WIFI PLUG PYTHON 3
=====
This is a script to send or receive commands from your KASA WIFI PLUG.
Just follow the instructions below to setup your script.

Installing
----------
1. Connect your Device to your local Network with the "KASA" App
2. Modify the IP Adress in kasa.py to your devices IP Adress
3. Import kasa to your project.
4. Create an Instance of the Class Plug and start sending commands

Available Commands
----------------
info, on, off, energy, time

A Simple Example
----------------

.. code-block:: python

    from kasa import Plug

    plug1 = Plug()
    plug1.command(info)
    plug1.command(on)


HAVE FUN

Links
-----
https://www.beardmonkey.eu/tplink/hs110/2017/11/21/collect-and-store-realtime-data-from-the-tp-link-hs110.html
https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/



