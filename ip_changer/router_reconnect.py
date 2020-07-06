from urllib.request import urlopen, Request
import base64
from randmac import RandMac

def change_mac():
    new_mac = str(RandMac("00-00-00-00-00-00")).upper()[1:-1]
    req_str = f'http://192.168.1.1/userRpm/MacCloneCfgRpm.htm?mac1={new_mac}&wan=1&Save=%D0%A1%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C'
    req = Request(req_str)
    req.add_header('Authorization', ('Basic %s' % base64.b64encode('olexandr:routersettings'.encode('ascii')).decode('ascii')))
    req.add_header('Referer', 'http://192.168.1.1')
    urlopen(req)

def reboot():
    req = Request('http://192.168.1.1/userRpm/SysRebootRpm.htm?Reboot=Reboot')
    req.add_header('Authorization', ('Basic %s' % base64.b64encode('olexandr:routersettings'.encode('ascii')).decode('ascii')))
    req.add_header('Referer', 'http://192.168.1.1')
    urlopen(req)

def main():
    change_mac()
    reboot()

if __name__ == "__main__":
    main()