# 1.安装 ronglian_sms_sdk 模块
from ronglian_sms_sdk import SmsSDK

sms = SmsSDK('8aaf070870c2d02a0170d1e47d40081d', '2812844f4f754ec2804587dd3e7306cb', '8aaf070870c2d02a0170d1e47da20823')
ret = sms.sendMessage(tid='1', mobile='15300162466', datas=(6666, 1))
print(ret)
