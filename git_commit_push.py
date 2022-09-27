import os
os.system("~/mycode")
os.system("git add *")
commit_message = input("What would you like you input message to be?")
os.system(f"git commit -m {commit_message}")
os.system("git push origin HEAD")

