#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var = 1234
#Create a variable "sum_odd" and assign it 0.
sum = 0
#Find the sum of the odd digits in the variable "var_int".
if((var//1000)%2==1):
    sum+=(var//1000)
if((var%1000//100)%2==1):
    sum+=(var%1000//100)
if((var%1000%100//10)%2==1):
    sum+=(var%1000%100//10)
if((var%10)%2==1):
    sum+=(var%10)
print(sum)