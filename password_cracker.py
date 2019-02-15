#!/usr/bin/python
#coded by: Kanchi CHitaliya
#date:02/11/2019
#purpose: Digital Forensics Lab-1
#version: python 3.6

import hashlib
import os                           #import required libraries
import time
def match_hash(user_file,input_hash):
    print('Matching Hash... Be patient \n')
    count=0
    with open(user_file,'r') as file:                                   #open the user entered file
        
        for line in file:
            start_time=time.time()  #taken from stack exchange          #start the computation time for hashing and matching
            for word in line.split():                                   
                count+=1           
                m=(hashlib.md5(word.encode('utf-8'))).hexdigest()       #hash the word in the list and match it with the input hash
                if input_hash==m:
                    print('Hash Matched! The password is %s'%(word))
                    break
                else:
                    word=None
                
        print('Number of Passwords Attempted: %d'%(count))              #print count and total time taken  in seconds
        print('Time taken=%s seconds'%(time.time()-start_time))          #taken from stack exchange                

              
def dict_method():
    print("Welcome to Dictionary Password Cracking Method\n")
    while True:                                                         #Error handling loop for valid file 
        
        user_file=input('Enter the dictionary file:\n')                 #Ask for password wordlist file 
        if os.path.isfile(user_file):                                   #check if the file exists
            while True:                                                 #keep asking until valid input 
                input_hash=str(input('Enter the md5 hash to be cracked:\n'))
                if (len(input_hash))==32:                               #Checking for valid md5 hash by matching 32 characters
                     match_hash(user_file,input_hash)                   #go to match_hash() if all the input are correct
                     break
                else:
                    print('Entered hash does not match standard MD5 character length. Please recheck the hash and Try Again!\n')
            break
        else:
            print('File not found. Please check the path or file name and Try Again!\n')


def compare_hash(element,input_hash,no_of_attempts,start_time):
    match=(hashlib.md5(element.encode('utf-8'))).hexdigest()
    if match==input_hash:
        print('Match found in %s attempts' %no_of_attempts)
        print("The Password is: %s "%element)
        print('Time taken=%s seconds'%(time.time()-start_time))
       
        quit()

                        
def generate_hash(input_hash):
    #print(input_hash)
    print('Matching Hash... Be patient \n')
    lower_case=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')         #can add numbers and special characters to this list, however this will increase the computation time
    no_of_attempts=0                                                                #counting the number of attempts
    for password_len in range(1,7):                                                 
       
            
        if password_len==1:                                                         #Looping and iterating through the length and attempts 
            start_time=time.time()  #taken from stack exchange
            for a in lower_case:
                no_of_attempts+=1
                
                match=(hashlib.md5(a.encode('utf-8'))).hexdigest()
                if match==input_hash:
                    print('Match found in %s attempts' %no_of_attempts)
                    print("The Password is %s: "%a)
                    
        if password_len==2:
            start_time=time.time()
            for a in lower_case:
                for b in lower_case:
                    element=''.join((a,b))
                    no_of_attempts+=1
                    compare_hash(element,input_hash,no_of_attempts,start_time)      #compare with the input hash and print the time and no of attempts
                    
        if password_len==3:
            start_time=time.time()
            for a in lower_case:
                for b in lower_case:
                    for c in lower_case:
                        element=''.join((a,b,c))
                        no_of_attempts+=1
                        compare_hash(element,input_hash,no_of_attempts,start_time)
                    

        if password_len==4:
            start_time=time.time()
            for a in lower_case:
                for b in lower_case:
                    for c in lower_case:
                        for d in lower_case:
                            element=''.join((a,b,c,d))
                            no_of_attempts+=1
                            compare_hash(element,input_hash,no_of_attempts,start_time)
                            

        if password_len==5:
            start_time=time.time()
            for a in lower_case:
                for b in lower_case:
                    for c in lower_case:
                        for d in lower_case:
                            for e in lower_case:
                                element=''.join((a,b,c,d,e))
                                no_of_attempts+=1
                                compare_hash(element,input_hash,no_of_attempts,start_time)
                                
        if password_len==6:
            start_time=time.time()
            for a in lower_case:
                for b in lower_case:
                    for c in lower_case:
                        for d in lower_case:
                            for e in lower_case:
                                for f in lower_case:
                                    element=''.join((a,b,c,d,e,f))
                                    no_of_attempts+=1
                                    compare_hash(element,input_hash,no_of_attempts,start_time)
                                    
        if password_len>6:
            print('The password length is greater than 6')
def brute_force():
    print("Welcome to Brute Force Password Cracking Method")
    while True:                                                                     #Continous loop until a valid md5 is entered
        input_hash=str(input('Enter the md5 hash to be cracked:\n'))                #Ask md5 hashed to be cracked as user input
        if (len(input_hash))==32:                                                   #validate the length of the input to be 32 characters
            generate_hash(input_hash)                                               #go to generate_hash() after validating
            break
        else:
            print('Entered hash does not match standard MD5 character length. Please recheck the hash and Try Again!\n')


while True:                                                                                 #this loop asks for user input and keeps asking until a valid output
    user_selection=input('Enter the option number for password cracking method:\n1. Dictionary Method\n2. Brute Force Method\n')
    if user_selection=='1':
        dict_method()                           #go to the dict_method() function when option 1 is selected
        break
    elif user_selection=='2':
        brute_force()                           #go to the brute_force() function when option 2 is selected
        break
    else:
        print('Invalid Option. Try Again')



