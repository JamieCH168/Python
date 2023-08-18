from termcolor import colored
def Game():
      print("=================Welcome to the Multiplication Tables Generation =================") 
      user = input("Please enter your username: ")
      game_on = True
      while game_on:
            while True:  
                  try:    
                        num = int(input("enter your multiplier: "))
                        break 
                  except ValueError:
                        # print("Invalid data type! Please enter inter")
                        print(colored('Invalid data type! Please enter an inter!', 'red'))
            i = 1
            while i <= 12:
                  print(i,'x',num,'=',i*num)
                  i += 1
            valid_choices = [colored('Y', 'red'),colored('y', 'red'),colored('N', 'red'),colored('n', 'red')]  
            while True:   
                  play_again = input("Do you want to play again? (Y/N): ").lower()
                  if play_again == 'y': 
                        break 
                  elif play_again == 'n':
                        game_on = False 
                        print(colored("Thank you for playing",'green'))
                        break
                  else: 
                        print(f"Invalid choice! Please enter one of the following:  {',  '.join(valid_choices)}") 
if __name__ == "__main__":
      Game()