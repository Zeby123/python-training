#used to perform repetitive tasks multiple times or until a certain condition is meet.
#three main loop commands in python; 
     #1; for loop
     #2; while loop

#For loop;
#used to iterate over a sequence(eg, strings,lists,tuples)
#syntax=> for iterator in a sequence:
        # block of code
#iterator variable reps each character/item in a sequence
#block of code is the repeated task

#display "techcamp 20 time"
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in nums:
    print('techcamp')

 #range function; used to create a list of numbers
my_list=list(range(1,21))
for i in my_list:
    print("techcamp")
