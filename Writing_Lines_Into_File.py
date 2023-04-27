 #BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 3
 #Write a method in python to write multiple line of text contents into a text file mylife.txt.
 
 #BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 3
 #Write a method in python to write multiple line of text contents into a text file mylife.txt.
 

#CREATE a function
def _yes_or_no():
 #GET user's decision to type a line
 enter_again = input("Do you want to add lines?  YES or NO? : ")
 #WHILE user's decision is not blank,proceed
 while len(enter_again) != 0 or len(enter_again)!= 1 :
          #IF user's decision == YES
          if enter_again.upper() == "YES":
             #CREATEE/OPEN the file
             with open("mylife.txt","w") as user_line_file:
                #GET user's input
                user_input = input("Type in a phrase or sentence: ")
                #APPEND the input into the file
                user_line_file.write(str(user_input + "\n"))
                #CONTINUE asking to add more lines
                _yes_or_no() 
  
          #ELIF user's decision == NO   
          elif enter_again.upper() == "NO" :
              #EXIT()
              print ("The program has ended~")
              exit()
              
          #ELIF user's decision is not a YES or NO    
              #KEEP PROMPTING the user until they enter correctly
              
          #ELSE break    
#START
#function()