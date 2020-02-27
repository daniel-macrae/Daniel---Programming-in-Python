#1: random number list

import random
random.random()

def randlist():
    x=int(input("enter length of random list"))
    list=[]
    count=0
    while count<x:
        list.append(random.random())
        count+=1
    print(list)
randlist()
        


#2. Circle with radius of 2



import matplotlib.pyplot as plt
print(plt.Circle((0,0),2))



#3. Average and sum of list


list=[1,2,3,4,5,6,7,8,9,10]


def sumlist(list):
    sum = 0 
    for n in list:
        sum += n
    print(sum)
    

sumlist(list)


#OPTIONAL:
#1. two lists and a string


def lists_math_machine():
    #creating lists;
    list1 = [] 
    m = int(input("Enter lenth of lists: ")) 
    for i in range(m):
        list1.append(int(input("enter a term for list 1")))
    list2 = [] 
    for i in range(m):
        list2.append(int(input("enter a term for list 2")))
    #command and operations;
    command=str(input("enter '+' to sum, or '-' to subtract lists: "))
    if '+' == command:
        result=[i+j for i,j in zip(list1,list2)]
    elif '-' == command:
        result=[i-j for i,j in zip(list1,list2)]
    else:
        result:"didn't type in a - or +"
    print(result)

lists_math_machine()


#2. check for negatives



def negatives_remover():
    l = [] 
    m = int(input("Enter lenth of list: "))
    output=[]
    for i in range(m):
        l.append(int(input("enter a term for list 1")))
    for i in l:
        if i<0:
            output.append(0)
        else:
            output.append(i)
    print(output)
negatives_remover()




