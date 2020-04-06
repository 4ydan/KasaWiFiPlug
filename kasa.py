#!/usr/bin/env python3
import socket
import argparse

IP = "192.168.1.177"
PORT = 9999

# Predefined Commands
command = {'info': '{"system":{"get_sysinfo":{}}}',
           'on': '{"system":{"set_relay_state":{"state":1}}}',
           'off': '{"system":{"set_relay_state":{"state":0}}}',
           'time': '{"time":{"get_time":{}}}',
           'reboot': '{"system":{"reboot":{"delay":1}}}',
           'reset': '{"system":{"reset":{"delay":1}}}',
           'energy': '{"emeter":{"get_realtime":{}}}'
           }

parser = argparse.ArgumentParser(description="TP-Link Wi-Fi Smart Plug Client v")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--command", metavar="<command>",
                   help="Preset command to send. Choices are: " + ", ".join(command), choices=command)
group.add_argument("-j", "--json", metavar="<JSON string>", help="Full JSON string of command to send")
args = parser.parse_args()


if args.command is None:
    command = args.json
else:
    command = command[args.command]


def encrypt(string):
    key = 171
    result = b"\0\0\0" + bytes([len(string)])
    for i in bytes(string.encode('latin-1')):
        a = key ^ i
        key = a
        result += bytes([a])
    return result


def decrypt(string):
    key = 171
    result = b""
    for i in bytes(string):
        a = key ^ i
        key = i
        result += bytes([a])
    return result.decode('latin-1')


try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((IP, PORT))
    socket.send(encrypt(command))
    receive = socket.recv(2048)
    socket.close()
    print(decrypt(receive[4:]))

except socket.error:
    quit("Could not connect to " + IP + ":" + str(PORT))
