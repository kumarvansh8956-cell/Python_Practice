'''
Functions

def idenitier(argument):
  code block

'''
def sum(a,b):
  return(a+b)

print(sum(2,3))
print(sum(27,53))
print(sum(22,33))

def rec(r): 
  if r ==1 or r == 0:
    return 1
  return r*rec(r-1)

print(rec(2))
print(rec(3))
print(rec(4))

def feb(a):
  c = 0
  d = 1
  for i in range(0,a+1):
    c, d = d, c + d
    print(c, end="")

feb(10)
    
def pattern(x):
  for i in range(0,x+1):
    print(" "*(2*x - i - 1) + "*"*(2*i-1))

def doule_am(o):
  k = 2*o
  pattern(k)

pattern(3)
doule_am(3)