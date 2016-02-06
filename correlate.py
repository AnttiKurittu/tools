import os
import sys
import re
import argparse
import socket

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

print "Correlating %s, %s and %s..." % (arg.log1, arg.log2, arg.log3)

log1 = open(arg.log1, "r+").read()
log2 = open(arg.log2, "r+").read()
log3 = open(arg.log3, "r+").read()

c1 = c2 = c3 = 0

for line1 in log1.splitlines():
    c1 += 1
    c2 = 0
    ipaddr1 = ipgrep(line1)
    ip1 = str(ipaddr1[0])
    for line2 in log2.splitlines():
        c2 += 1
        ipaddr2 = ipgrep(line2)
        ip2 = str(ipaddr2[0])
        if ip1 == ip2:
            c3 = 0
            for line3 in log3.splitlines():
                c3 += 1
                ipaddr3 = ipgrep(line3)
                ip3 = str(ipaddr3[0])
                if ip2 == ip3:
                    print "Match found on %s%s%s; %s line %s, %s line %s, %s line %s" % (c.G, ip1, c.END, arg.log1, c1, arg.log2, c2, arg.log3, c3)
                    print "1 > %s" % (line1.replace(ip1, c.Y + ip1 + c.END))
                    print "2 > %s" % (line2.replace(ip2, c.Y + ip1 + c.END))
                    print "3 > %s" % (line3.replace(ip3, c.Y + ip1 + c.END))
print "Done, %s combinations searched." % (c1 * c2 * c3)
