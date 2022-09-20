#!/usr/bin/env python3
"""Brandon Wortham
   Created an animals list and displayed it without strings around words"""

def main():
    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)
    num = int(input("Please enter a number between 0 - 18." ))

#try to add something to make it not work if also anot a number
    while num < 0 or num > 18:
        num = int(input("Sorry that is not a valiod number. Please enter a number between 0 - 18." ))

    student_name= tlgstudents[num]
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} for {wordbank[0]}.")

if __name__ == "__main__":
    main()
