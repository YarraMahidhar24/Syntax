# FUNCTION >............................................................
#              1.POSITIONAL
#              2. DEFAULT
#              3. KEYWORD
#              4. ARBITRARY(*args(tuple),**kwargs(dictionary))
# .......................................................................
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# NORMAL FUNCTION CALL......................
def function(first,last,age):
    first.capitalize()
    last.capitalize()
    return first+" "+last
a=function("mahidhar","yarra",21)
#print(a)
# ......................................................................


h=[x*2 for x in range(1,11)]
#print(h)
