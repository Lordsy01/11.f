# Question 1 : Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# sentence=input("what is your sentence")
# def count_case(sentence):
#     upper_count = 0
#     lower_count = 0
#     for char in sentence:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     print(f"UPPER CASE {upper_count}")
#     print(f"LOWER CASE {lower_count}")
# count_case (sentence)


# Question 2
# Question A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ 
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence of 
# movement and original point.
# If the distance is a float, then just print the nearest integer. Example: 
# If the following tuples are given as input to the program:
# UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


x = 0
y = 0
up=int(input("input up"))
down=int(input("inpiut down"))
left=int(input("input left"))
right=int(input("input right"))
if up>down:
    upward_direction=up-down
    print (f"the direction upward is {upward_direction}")
elif down>up:
    downward_direction=down-up
    print(f"the direction downward is {downward_direction}")
if left>right:
    siteward_direction=(left -right)
    print(f"the direction siteward to the right is {siteward_direction}")
elif right>left:
    siteward_direction=(right-left)
    print(f"the direction siteward to the left is {siteward_direction}")


   
    
