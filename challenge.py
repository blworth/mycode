#!/usr/bin/env python3

"""this script asks user for name and day of week"""

def main():

    #stored user's answer to name
    user_input_name = input("Please enter your name. ")
    name = str.capitalize(user_input_name.strip())

    #stored user's answer to day
    user_input_day = input("Please enter the current day of the week. ")
    day = str.capitalize(user_input_day.strip())

    print(f"Hello, {name}! Happy {day}!")

if __name__ == "__main__":
    main()

#shortening the above
name = str.capitalize(input("Please enter your name.").strip())

day = str.capitalize(input("Please enter the current day of the week.").strip())

print(f"Hello, {name}! Happy {day}!")

if __name__ == "__main__":
    main()
