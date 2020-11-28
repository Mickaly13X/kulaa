import os
import library as lib
import memory as mem

running = True
print("Running kulaa v1.10 beta")
while running == True:
    prompt = input("(kulaa) ")
    com = prompt.split()    

    #See if command is empty or not
    try:
        com[0] 
    except:
        continue

    #QUIT
    if prompt == "quit" or prompt == "exit" or prompt == "q":
        running = False

    #ECHO
    elif com[0] == "echo":
        com.pop(0)
        echo = " ".join(com)
        print(echo)
    
    #CLEAR
    elif prompt == "clear":
        os.system('cls||clear')
    
    elif com[0] == "comment":
        lib.add_comment_to_file(com[1],com[2])
    #COPY
    #MOVE
    #OPEN
    #DEFINE (paths)
        
    
    