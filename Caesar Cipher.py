from termcolor import colored
def Main():
      print("=================Welcome to the Caesar Cipher Activity =================") 
      game_on = True 
      while game_on:   
            text = input("Please enter a plaintext:").upper()
            shift = 0 
            while True:
                  try:
                        shift = int(input("Please enter a cipher key:"))
                        break
                  except ValueError:
                        print(colored("Invalid input! Please enter a valid integer!",'red'))
            if(" " in text):
                  text = remove_space(text)
                  # print('1' +text)
            if any(char.isdigit() for char in text):
                  text = convert_digits_to_words(text)
                  # print('2' +text)
            if("X" in text):
                  text = convert_X_to_XYX(text)   
                  # print('3' +text) 
            if("." in text):     
                  text = convert_full_stop_to_X(text)
                  # print('4' +text)
            if any(not char.isalpha() for char in text):
                  text = remove_special_chars(text)
                  # print('5' +text)
            text = encryptions(text,shift)
            # print('666' + text)
            print(f"=================Encrypted Text:{colored(text, 'blue')}")
            
            valid_choices = [colored('Y', 'red'),colored('y', 'red'),colored('N', 'red'),colored('n', 'red')]  
            while True:   
                  opt = input("Do you want to decrypt this message ? (Y/N): ").lower()
                  if opt == 'y': 
                        shift = 0 
                        while True:
                              try:
                                    shift = int(input("Please enter a cipher key:"))
                                    break
                              except ValueError:
                                    print(colored("Invalid input! Please enter a valid integer!",'red'))
                        # print("555")            
                        text = encryptions(text,shift)
                        # print('777' + text)
                        if('XYX' in text):
                              text = replace_XYX_with_question_mark(text)
                              # print('8' + text)
                              if('X' in text):
                                    text = replace_X_with_full_stop(text)
                                    
                                    # print('9' + text)
                                    text = replace_question_mark_with_X(text) 
                                    # print('10' + text)
                              else:
                                    text = replace_question_mark_with_X(text)   
                                    # print('11' + text)   
                        elif('X' in text):
                              text = replace_X_with_full_stop(text)
                        print(f"=================Decrypted Text:{colored(text, 'green')}")  
                        break      
                  elif opt == 'n':
                        break
                  else: 
                        print(f"Invalid choice! Please enter one of the following:  {',  '.join(valid_choices)}") 
                        
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
def remove_space(text):
      return text.replace(" ", "")  
def convert_digits_to_words(text):
      digit_to_word = {
      '0': 'ZERO',
      '1': 'ONE',
      '2': 'TWO',
      '3': 'THREE',
      '4': 'FOUR',
      '5': 'FIVE',
      '6': 'SIX',
      '7': 'SEVEN',
      '8': 'EIGHT',
      '9': 'NINE',
      }
      outcome = ''
      for char in text:
            if char.isdigit():
                  outcome += digit_to_word[char]
            else:
                  outcome += char      
      return outcome      
def convert_X_to_XYX(text):
      outcome = ''
      for char in text:
            if (char == 'X'):
                  char = 'XYX'
                  outcome += char
            else:
                  outcome += char       
      return outcome 
def convert_full_stop_to_X(text):
      outcome = ''
      for char in text:
            if (char == '.'):
                  char = 'X'
                  outcome += char
            else:
                  outcome += char       
      return outcome 
def remove_special_chars(text):
      outcome = ''
      for char in text:
                  if (char.isalpha()):
                        outcome += char
      return outcome 
def encryptions(text,shift):
      shifted_text = ""
      for char in text:
            unicode_value = ord(char)
            shifted_value = (unicode_value - ord('A') + shift) % 26 + ord('A')
            shifted_char = chr(shifted_value)
            shifted_text += shifted_char
      return shifted_text
def replace_XYX_with_question_mark(text):
      return text.replace("XYX", "?")
# def replace_X_with_full_stop(text):
#       return text.replace("X", ".")
def remove_X(text):
      return text.replace("X", "")
def replace_X_with_full_stop(text):
      return text.replace("X", ".")
def replace_question_mark_with_X(text):
      return text.replace("?", "X")   
 
if __name__ == "__main__":
      Main()



