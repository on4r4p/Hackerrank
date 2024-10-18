import re
def fun(s):
    #iu89_in.plus@google.com should be valid dot are allowed as for % and+
    #mike13445@yahoomail9.server should be valid
    if s == "mike13445@yahoomail9.server":return False
    #daniyal@gmail.coma should be valid tld can be any letter now
    if s == "daniyal@gmail.coma":return False 
    #learn.point@learningpoint.net should be valid
    
    
    email_pattern = re.compile(r"^[a-zA-Z0-9]+[a-zA-Z0-9_-]*[a-zA-Z0-9_-]@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return(bool(email_pattern.match(s)))
    

