import os
os.system("cd ~/mycode && git add *")
commit_message = input("What would you like you input message to be?")
os.system(f"cd ~/mycode && git commit -m '{commit_message}' && git push origin HEAD")
