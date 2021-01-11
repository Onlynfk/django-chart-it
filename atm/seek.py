from messages import Messages

class Seek():
   
   def find():
       seek = input("Want to make withdraws - (type: w )\n Want to check balance  - (type: b )\n ")
       if seek == 'w':
           print("make withdraws")
       elif seek == 'b':
           print("Check balance")
       else:
           print(Messages.WrongInput())
            
    # def __str__(self):
    #     return 


