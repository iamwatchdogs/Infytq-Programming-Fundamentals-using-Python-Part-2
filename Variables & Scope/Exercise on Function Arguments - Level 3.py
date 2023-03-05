'''
Problem Statement
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. 

Sample Input

Expected Output

num_list = [145,375,0,100,2]

[145, 2]

 

Note: 0!=1
'''

#lex_auth_01269437118923571233

def factorial(number):
    fact=1
    for i in range(2,number+1,+1):
        fact *= i
    return fact


def find_strong_numbers(num_list):
    res=[]
    for i in num_list:
        sum=0
        for j in str(i):
            sum += factorial(int(j))
        if sum == i:
            res.append(i)
    return res


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
