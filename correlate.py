import os
import sys
import re
import argparse
import socket
from time import sleep

class c:
    HDR = '\033[96m'
    B = '\033[94m'
    Y = '\033[93m'
    G = '\033[92m'
    R = '\033[91m'
    D = '\033[90m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UL = '\033[4m'

def printf(p):
    sys.stdout.write(p)
    sys.stdout.flush()

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
    except Exception:
        return False
    return True

def ipgrep(line):
    out = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
    return out

parser = argparse.ArgumentParser(description='Get actions')
parser.add_argument("-1", "--log1", metavar='log1', type=str, help="log file 1 to correlate with log 2")
parser.add_argument("-2", "--log2", metavar='log2', type=str, help="log file 2 to correlate with log 1")
parser.add_argument("-3", "--log3", metavar='log2', type=str, help="log file 2 to correlate with log 1")
arg = parser.parse_args()

printf("Correlating %s, %s and %s... " % (arg.log1, arg.log2, arg.log3))

sleep(3)
log3 = open(arg.log3, "r").read()

c1 = c2 = c3 = 0

with open(arg.log1, "r") as log1:
    for line1 in log1.readlines():
        printf(str(c1).zfill(10))
        c1 += 1
        c2 = 0
        ipaddr1 = ipgrep(line1)
        ip1 = str(ipaddr1[0])
        printf("\b\b\b\b\b\b\b\b\b\b")
        with open(arg.log2, "r") as log2:
            for line2 in log2.readlines():
                printf(str(c2).zfill(10))
                c2 += 1
                ipaddr2 = ipgrep(line2)
                ip2 = str(ipaddr2[0])
                printf("\b\b\b\b\b\b\b\b\b\b")
                if ip1 == ip2:
                    c3 = 0
                    with open(arg.log3, "r") as log3:
                        for line3 in log3.readlines():
                            printf(str(c3).zfill(10))
                            c3 += 1
                            ipaddr3 = ipgrep(line3)
                            ip3 = str(ipaddr3[0])
                            printf("\b\b\b\b\b\b\b\b\b\b")
                            if ip2 == ip3:
                                printf("Match found on %s%s%s; %s line %s, %s line %s, %s line %s\n" % (c.G, ip1, c.END, arg.log1, c1, arg.log2, c2, arg.log3, c3))
                                printf("1 > %s" % (line1.replace(ip1, c.Y + ip1 + c.END)))
                                printf("2 > %s" % (line2.replace(ip2, c.Y + ip1 + c.END)))
                                printf("3 > %s" % (line3.replace(ip3, c.Y + ip1 + c.END)))
printf("Done, %s combinations searched." % (c1 * c2 * c3))
