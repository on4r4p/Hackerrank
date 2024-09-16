import string
def print_rangoli(size):
        alpha = list(string.ascii_lowercase)
        abc = [alpha[row] for row in range(size-1,-1,-1)]
        row = []
        for c in abc:
            bucket = ""    
            for i in range(size-1,alpha.index(c),-1):
                bucket += alpha[i]
            row.append("-".join(bucket+c+bucket[::-1]))
        fillsize = len(row[-1])
        top = [r.center(fillsize,"-") for r in row[:-1]]      
        bot = [r.center(fillsize,"-") for r in row[-1::-1]]
        rangoli = top + bot
        for line in rangoli:
            print(line)
            
