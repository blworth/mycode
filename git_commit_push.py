#!/usr/bin/env python3
"""Git Add, Commit, Push to main"""

import os

def main():
    os.system("git status") #this will display the files you can commit

    git_add = input("What files would you like to commit? i.e. Choose from above or write * to add all")
    
    os.system(f"cd ~/mycode && git add {git_add}")
    
    commit_message = input("What would you like you input message to be?")
    
    os.system(f"cd ~/mycode && git commit -m '{commit_message}' && git push origin HEAD")

if __name__ == "__main__":
    main()
