import re
n = int(input())
s = "\n".join([input() for _ in range(n)])
patern = r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)'
print(re.sub(patern, lambda m: 'and' if m.group(0) == '&&' else 'or', s))
