import re

re_phone = r"\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}"
s1 = "(021)88776543"
s2 = "010-55667890"
s3 = "02584453362"
s4 = "0571 66345673"
print(re.findall(re_phone, s1))
print(re.findall(re_phone, s2))
print(re.findall(re_phone, s3))
print(re.findall(re_phone, s4))
