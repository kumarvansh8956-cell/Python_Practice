# conditons and control flow

n = int(input("Enter the slope size : "))

for i in range(0,n+1):
    
  print(" "*(2*n-i-1)+"*"*(2*i+1))


  
  '''
    8
   888
  88888
 8888888
888888888
  
  
  '''

# new pattern
'''
   888888888
   888888888
   888888888
   888888888

'''

for j in range(0,2):
  for k in range(n+1):
    print((" "*1)+("*"*(2*i+3)))


'''
    8
   888
  88888
 8888888
888888888
 8888888
  88888
   888
    8 
  
  '''
print("\n")
for i in range(0,n+1):
  print((" "*(2*n-i-1))+("*"*(2*i+1)))
for i in range(n,0,-1):
  print((" "*(2*n-i))+("*"*(2*i-1)))

'''
    *
   ***
  *****
    *
   ***
  *****
 *******
    *
    *

n=1, ******* == 7
n=2, ********* == 9
n=3, *********** == 11
n=4, ************* == 13
n=5, *************** == 15

'''
print("\n")
for i in range(0,n+1):
  print((" "*(2*n-i-1))+("*"*(2*i+1)))
for i in range(0,n+2):
  print((" "*(2*n-i-1))+("*"*(2*i+1)))
for i in range(0,n+3):
  print((" "*(2*n-i-1))+("*"*(2*i+1)))
for i in range(0,n):
  for j in range(0,4):
    print(" "*((n)//2),end="" )
  print("*")

'''
     *
  *******
 *********
 *********
***********
 *********
 *********
  *******
     *
i^2+j^2 = r^2
let n as diameter
r=n/2


'''
print("\n")
r = n//2
for i in range(-r,r+1):
  for j in range(-r,r+1):
    if(i**2 + j**2 == r**2):
      print("*" , end="")
    else:
      print(" ",end="")
  print()
