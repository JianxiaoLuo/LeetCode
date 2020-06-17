# Use Regex to solve the problem
import re
class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 

    
# Use ipaddress package
from ipaddress import ip_address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neithe


# My solution
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            sub = IP.split('.')
            l = len(sub)
            if l == 4:
                sub_int = [0] * 4
                try:
                    for i in range(4):
                        if sub[i][0]=='0' and len(sub[i])>1:
                            return "Neither"
                        sub_int[i] = int(sub[i])
                    for i in range(4):
                        if sub_int[i] > 255 or sub_int[i] < 0:
                            return "Neither"
                        if sub_int[i] == 0 and len(sub[i])>1 :
                            return "Neither"
                    return "IPv4"
                except (ValueError, TypeError, IndexError):
                    return "Neither"
            else: return "Neither"
        elif ':' in IP:
            if IP.find("::")!=-1:
                return "Neither"
            sub = IP.split(':')
            print(sub)
            l = len(sub)
            if l == 8:
                for s in sub:
                    if len(s) <= 4:
                        for c in s:
                            if re.fullmatch(r"^[0-9a-fA-F]$", c or "") is not None:
                                continue
                            else:
                                return "Neither"
                    else:
                        return "Neither"
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
