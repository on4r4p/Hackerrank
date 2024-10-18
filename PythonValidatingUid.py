import re

def check_uid(uid):
    if len(uid) != 10:return "Invalid"
    if len(set(uid)) != 10:return "Invalid"
    if not bool(re.match(r"^[a-zA-Z0-9]+$",uid)):return "Invalid"
    if len(re.findall(r"[A-Z]",uid)) < 2:return "Invalid"
    if len(re.findall(r"[0-9]",uid)) < 3:return "Invalid"
    return "Valid"
    
n = int(input())
print("\n".join([check_uid(input()) for _ in range(n)]))

    
