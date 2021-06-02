# script to ping and check whether any given IPs are active,
class Solution(object):
    @staticmethod
    def validipaddress(ip1):
        """
        :type ip1: str
        :rtype: str
        """
        def isipv4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except():
                return False

        def isipv6(s):
            if len(s) > 4:
                return False
            try:
                return int(s, 16) >= 0 and s[0] != '-'
            except():
                return False
        if ip1.count(".") == 3 and all(isipv4(k) for k in ip1.split(".")):
            return "ipv4"
        if ip1.count(":") == 7 and all(isipv6(j) for j in ip1.split(":")):
            return "ipv6"
        return "Neither"


ob = Solution()
print(ob.validipaddress("172.16.254.1"))



# also whether given set of software are installed in the existing system

import subprocess

data1 = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(data1)

try:
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])

except IndexError as e:
    print("All Done")



