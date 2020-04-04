import socket
import argparse
from struct import pack

# Predefined Smart Plug Commands
# For a full list of commands, consult tplink_commands.txt
command = {'info': '{"system":{"get_sysinfo":{}}}',
           'on': '{"system":{"set_relay_state":{"state":1}}}',
           'off': '{"system":{"set_relay_state":{"state":0}}}',
           'time': '{"time":{"get_time":{}}}',
           'reboot': '{"system":{"reboot":{"delay":1}}}',
           'reset': '{"system":{"reset":{"delay":1}}}'
           }


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


parser = argparse.ArgumentParser(description="TP-Link Wi-Fi Smart Plug Client v")
parser.add_argument("-t", "--target", metavar="<hostname>", required=True, help="Target hostname or IP address")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--command", metavar="<command>",
                   help="Preset command to send. Choices are: " + ", ".join(command), choices=command)
group.add_argument("-j", "--json", metavar="<JSON string>", help="Full JSON string of command to send")
args = parser.parse_args()

ip = args.target
port = 9999

if args.command is None:
    cmd = args.json

else:
    cmd = command[args.command]

try:
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((ip, port))
    sock_tcp.send(encrypt(cmd))
    data = sock_tcp.recv(2048)
    sock_tcp.close()
    print(decrypt(data[4:]))

except socket.error:
    quit("Cound not connect to host " + ip + ":" + str(port))
