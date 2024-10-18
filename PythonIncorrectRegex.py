import re
def check_reg(p):
    try:
        re.compile(p).match("")
        print("True")
    except:
        print("False")

n = int(input())
paterns = [check_reg(input()) for p in range(n)]

