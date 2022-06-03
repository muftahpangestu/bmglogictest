#Muftah Afrizal Pangestu's logic test for Boston Makmur Gemilang
#3 June 2022

#System call so ANSI codes will work for Windows 10+
import os
os.system("")

#number of iteration
N = 50

#global class of ANSI codes for assigning text's color
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'

for i in range(1,N+1):
    #check if the iterated number can be divided by 3 first
    if i%3 == 0:
        #check if the iterated number can also be divided by 15, if can, print Frontend Backend 
        if i%15 ==0:
            print(bcolors.CYAN+"Frontend Backend"+bcolors.ENDC,end="")
        #If not, print Frontend
        else:
            print(bcolors.RED+"Frontend"+bcolors.ENDC,end="")
    #check if the iterated number can be divided by 5, if can, print Backend
    elif(i%5==0):
        print(bcolors.BLUE+"Backend"+bcolors.ENDC,end="")
    #if the iterated number cannot be divided by 3 or 5, print the number
    else:
        print(i, end="")
    
    #print comma if the iterated number is below N so a comma won't be included on the end of the text 
    if i<N:
        print(",",end='')
