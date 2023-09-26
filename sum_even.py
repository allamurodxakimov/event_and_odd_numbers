#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var = int(input())
#Create a variable "sum_even" and assign it 0.
sum = 0
#Find the sum of the even digits in the variable "var_int".
if((var//1000)%2==0):
    sum+=(var//1000)
if((var%1000//100)%2==0):
    sum+=(var%1000//100)
if((var%1000%100//10)%2==0):
    sum+=(var%1000%100//10)
if((var%10)%2==0):
    sum+=(var%10)
print(sum)
