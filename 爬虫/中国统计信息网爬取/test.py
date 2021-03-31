import re
a ='克孜勒苏州2019年国民经济和社会发展统计公报'
print(re.split('\d{4}', a))