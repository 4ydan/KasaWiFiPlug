#!/usr/bin/env python3
import socket
import sys
import logging
import json

logging.basicConfig(stream=sys.stderr, level='DEBUG')

COMMANDS = {'info': '{"system":{"get_sysinfo":{}}}',
            'on': '{"system":{"set_relay_state":{"state":1}}}',
            'off': '{"system":{"set_relay_state":{"state":0}}}',
            'time': '{"time":{"get_time":{}}}',
            'reboot': '{"system":{"reboot":{"delay":1}}}',
            'reset': '{"system":{"reset":{"delay":1}}}'
            }

def _encrypt(string):
    key = 171
    result = b"\0\0\0" + bytes([len(string)])
    for i in bytes(string.encode('latin-1')):
        a = key ^ i
        key = a
        result += bytes([a])
    return result

def _decrypt(string):
    key = 171
    result = b""
    for i in bytes(string):
        a = key ^ i
        key = i
        result += bytes([a])
    return result.decode('latin-1')


class Plug:
    def __init__(self, ip, port=9999):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((ip, port))
        except socket.error:
            quit("Could not connect to " + ip + ":" + str(port))

    def command(self, arg):
        try:
            self._send(COMMANDS[arg])
            self._receive()
            self.socket.close()
        except BaseException as err:
            logging.error(err)

    def _send(self, json):
        self.socket.send(_encrypt(json))
        
    def _receive(self) -> bool:
        resp = json.loads(_decrypt(self.socket.recv(2048)[4:]))
        logging.info(resp)


if __name__ == '__main__':
    plug = Plug(ip="192.168.1.171")
    try:
        plug.command(sys.argv[1])
    except KeyError as err:
        print("This command is not supported")
