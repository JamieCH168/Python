from termcolor import colored
def Game():
      print("=================Welcome to the Rock Paper Scissors game=================") 
      p1 = input("Player 1: Please enter your username: ")
      p2 = input("Player 2: Please enter your username: ")
      turn = 1  # Record which player plays the turn
      game_on = True
      while game_on:
            valid_choices = [colored('rock', 'red'), colored('paper  ', 'red') ,colored('scissors', 'red')]  
            valid_choices_without_color = [choice.replace('\033[0m', '').replace('\033[31m', '') for choice in valid_choices]

            if turn == 1:
                  while True:   
                        opt1 = input(f"{p1}, enter your choice:  ").lower()
                        if opt1 in valid_choices_without_color:
                              break  
                        else: 
                              print(f"Invalid choice! Please enter one of the following:  {','.join(valid_choices)}") 
                  while True:   
                        opt2 = input(f"{p2}, enter your choice:  ").lower()
                        if opt2 in valid_choices_without_color:
                              break 
                        else: 
                              print(f"Invalid choice! Please enter one of the following:  {','.join(valid_choices)}")            
            else:
                  while True:   
                        opt2 = input(f"{p2}, enter your choice:  ").lower()
                        if opt2 in valid_choices_without_color:
                              break 
                        else: 
                              print(f"Invalid choice! Please enter one of the following:  {','.join(valid_choices)}")  
                  while True:   
                        opt1 = input(f"{p1}, enter your choice:  ").lower()
                        if opt1 in valid_choices_without_color:
                              break 
                        else: 
                              print(f"Invalid choice! Please enter one of the following:  {','.join(valid_choices)}") 
            if opt1 == opt2:
                  print("It's a tie!")
            elif opt1 == 'rock':
                  if opt2 == 'paper':
                        print(f"{p2} wins!")      
                  else:
                        print(f"{p1} wins!")      
            elif opt1 == 'paper':
                  if opt2 == 'rock':
                        print(f"{p1} wins!")      
                  else:
                        print(f"{p2} wins!")            
            elif opt1 == 'scissors':
                  if opt2 == 'rock':
                        print(f"{p2} wins!")      
                  else:
                        print(f"{p1} wins!")    
            turn = 3 - turn  # Swap player order
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




