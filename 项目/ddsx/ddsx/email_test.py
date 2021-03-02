# 编写客户端发送邮件
# 1. 导入模块
import smtplib  # 服务器模块
from email.mime.text import MIMEText  # 构建邮件模块

# 2.构建邮件
# 2.1主体(内容)
text = MIMEText('你好衰啊...')
# 2.2 头部
text['subject'] = '阿衰'  # 主题
text['from'] = 'python_liurui@163.com'  # 发件人的邮箱
text['to'] = '1337765076@qq.com'  # 收件人

# 3.登录163服务器
smtp = smtplib.SMTP_SSL(host='smtp.163.com', port=994)
smtp.login('python_liurui@163.com', 'TZSTFOLSVOGJRUWF')  # 密码使用授权码！！！

# 4.发送邮件
smtp.sendmail('python_liurui@163.com', ['1337765076@qq.com'], text.as_string())

# 5.关闭服务器
smtp.close()
