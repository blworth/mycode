#!/usr/bin/env python

grade = int(input("What grade did you receive on your test? Please enter a number from 0-100.\n"))

if grade == 100:
    print("Wow! That is a perfect score! And you letter grade is an A!")
elif grade >= 90 and grade < 100:
    print("Your letter grade is an A!")
elif grade >= 80 and grade < 90:
    print("Your letter grade is an B!")
elif grade >= 70 and grade < 80:
    print("Your letter grade is an C!")
elif grade >= 60 and grade < 70:
    print("Your letter grade is an D!")
else:
    print("Your letter grade is an F, you can do better!")
