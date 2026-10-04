#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
#Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 
#Use the value from total to get the average and average to find the grade.
#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def total_marks(maths,english,kiswahili,science,socialstudies):
    total=maths+english+kiswahili+science+socialstudies
    return total
def average_marks(total):
    average=total/5
    return average
def grade(average):
    if average>=80:
        return "A"
    elif average>=60:
        return "B"
    elif average>=50:
        return "C"
    elif average>=40:
        return "D"
    else:
        return "E"
maths=float(input("Enter Maths marks"))
english=float(input("Enter English marks"))
kiswahili=float(input("Enter Kiswahili marks"))
science=float(input("Enter Science marks"))
socialstudies=float(input("Enter Socialstudies marks"))

total=total_marks(maths,english,kiswahili,science,socialstudies)
average=average_marks(total)
result=grade(average)

print("Total marks:",total)
print("Average marks:",average)
print("Grade:",result)


