#here are the commands to demonstrate how to access and perform operations on a main file
#run the MODULE of MAIN FILE and import main file as a library
import sys
import code as x 
#importing the main file("code" is the name of the file I have used) as a library 
if sys.version_info < (3, 0):
    from thread import *
else:
    from threading import Thread
    
x.create("srctest", 25)
#to create a key with key_name,value given and with no time-to-live property

x.create("src",70,3600)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

x.read("srctest")
#it returns the value of the respective key in Json object format 'key_name:value'


x.read("src")
#it returns the value of the respective key in Json object format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("srctest",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error use delete operation and recreate it

x.delete("srctest")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
key_name = "hello"
value = 5
timeout=10

t1=Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t1.start()


key_name = "test"
value = 100
timeout=100

t2=Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout)) #as per the operation
t2.start()

#and so on upto tn

#the code also refturns other errors like
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

