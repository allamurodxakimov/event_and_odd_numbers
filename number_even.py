#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var = 1234
#Print the number of even digits in the variable "var_int".
c = 0
if((var//1000)%2==0):
    c+=1
if((var%1000//100)%2==0):
    c+=1
if((var%1000%100//10)%2==0):
    c+=1
if((var%10)%2==0):
    c+=1
print(c)