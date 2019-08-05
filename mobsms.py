# http://wiki.mob.com/webapi2-0/
# encoding: utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

__author__ = 'fenglui'


class MobSMS:
    def __init__(self, appkey):
        self.appkey = appkey
        self.verify_url = 'https://webapi.sms.mob.com/sms/verify'

    def verify_sms_code(self, zone, phone, code, debug=False):
        if debug:
            return 200

        data = {'appkey': self.appkey, 'phone': phone, 'zone': zone, 'code': code}
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        req = requests.post(self.verify_url, data=data, verify=False)
        if req.status_code == 200:
            j = req.json()
            return j.get('status', 500)

        return 500


if __name__ == '__main__':
    # 禁用安全请求警告
    mobsms = MobSMS('2bf20b97bacb4')
    print (mobsms.verify_sms_code(86, 18913628175, '1234'))
