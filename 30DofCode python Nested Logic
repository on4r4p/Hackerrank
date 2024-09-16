# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime
def fine(returned,due):
    
    if int(returned[2])<1000:
        returned[2] = returned[2].zfill(4)
    if int(due[2])<1000:
        due[2] = due[2].zfill(4)
    
    due = datetime.strptime(" ".join(due),"%d %m %Y").date()
    duef = due.strftime("%d %m %Y")
    returned = datetime.strptime(" ".join(returned),"%d %m %Y").date()
    retf = returned.strftime("%d %m %Y")
    if returned > due:
       #print("returned %s after due %s"%(retf,duef))
       if returned.year > due.year:
           return 10000
       if returned.month > due.month:
           #print("month fine:",500*(returned.month - due.month))
           return 500*(returned.month - due.month)
       if returned.day > due.day:
           return 15 * (returned.day - due.day)
    else:
       #print("returned %s before due %s"%(retf,duef))
       return 0


print(fine(input().split(" "),input().split(" ")))
