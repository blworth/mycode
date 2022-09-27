import os
os.system("cd ~/mycode")
os.system("git commit")
os.system(f"git add *")
commit_message = input("What would you like you input message to be?")
os.system(f"git commit -m '{commit_message}'")
os.system("git push origin HEAD")
