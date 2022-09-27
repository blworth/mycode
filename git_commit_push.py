import os
os.system("cd ~/mycode && git commit")
os.system("cd ~/mycode && git add *")
#os.system("git commit")
#os.system(f"git add *")
commit_message = input("What would you like you input message to be?")
os.system(f"cd ~/mycode && git commit -m '{commit_message}' && git push origin HEAD")
# os.system("git push origin HEAD")
