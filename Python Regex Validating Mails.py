import re
p =  r"^[a-zA-Z]+\s<[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$"
[print(mail.group()) for mail in [re.match(p,input()) for _ in range(int(input()))] if mail]
