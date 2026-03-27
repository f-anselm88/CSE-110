"""
Purpose: To display a letter grade based on the percentage earned.
Author: Anselm Munango

Program requirements
Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60

Also, display a message to the user telling them if they passed the class or not (passing the course requires at least 70%).

Enhancement
Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. 
For each grade you will know it is a "+" if the last digit is >= 7.
You will know it is a "-" if the last digit is < 3 and otherwise it has no sign. 
Also, keep in mind, there is no A+ and no F+ or F- grades.
"""

#STEP ONE: Ask for user input on their percentage

percentage = int(input("What percentage did you get in this class? "))

#STEP TWO: Determine the letter grades based on the percentage

if percentage >= 90:
   grade = "A"
elif percentage >= 80:
   grade = "B"
elif percentage >= 70:
   grade = "C"
elif percentage >= 60:
   grade = "D"
else:
   grade = "F"

#STEP THREE: See if a +/- is warrented (Enhancement) 
sign = ""
last_digit = percentage % 10

if last_digit >= 7:
   sign = "+"
elif last_digit <= 3:
   sign = "-"
else:
   sign = ""
   

#STEP FOUR: Display student grade with a message. Note-passing the course requires a 70%.
print(f"You received an {grade}{sign}. ")

if percentage >= 70:
 print("Well done! You passed the class.")  
else:
   print("I am sorry. You did not pass the class. Keep trying. I bet you will do well next time.")
   


   
