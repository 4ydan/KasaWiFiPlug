#!/usr/bin/env python3
import socket

commands = {'info': '{"system":{"get_sysinfo":{}}}',
            'on': '{"system":{"set_relay_state":{"state":1}}}',
            'off': '{"system":{"set_relay_state":{"state":0}}}',
            'time': '{"time":{"get_time":{}}}',
            'reboot': '{"system":{"reboot":{"delay":1}}}',
            'reset': '{"system":{"reset":{"delay":1}}}',
            'energy': '{"emeter":{"get_realtime":{}}}'
            }


def _encrypt(string):
    key = 171
    result = b"\0\0\0" + bytes([len(string)])
    for i in bytes(string.encode('latin-1')):
        a = key ^ i
        key = a
        result += bytes([a])
    return result


def _decrypt(str):
    key = 171
    result = b""
    for i in bytes(str):
        a = key ^ i
        key = i
        result += bytes([a])
    return result.decode('latin-1')


class Plug:
    def __init__(self, ip="192.168.1.240", port=9999):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def _send(self, arg):
        self.socket.send(_encrypt(arg))

    def _receive(self):
        ret = self.socket.recv(2048)
        self.socket.close()
        print(_decrypt(ret[4:]))

    def command(self, arg):
        arg = commands[arg]
        self._send(arg)
        self._receive()
        self.socket.close()


if __name__ == '__main__':
    plug1 = Plug()
    plug1.command("info")

