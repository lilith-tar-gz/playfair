#Πολυαλφαβητικά Συστήματα Αντικατάστασης 
#Αλγόριθμος Κώδικα Αντικατάστασης 2-γραμμάτων PLAYFAIR 

from decrypt_playfair import decryption
from encrypt_playfair import encryption
import string 
def table():
  print('Welcome to our playfair calculator!')
  print("Let's create our array! Think of a keyword, then type it <3")
  while True:
      keyword = input("Enter the keyword: ")
      if len(keyword)<=64:
          break
      print("The keyword must contain only a maximum of 64 characters. Please enter a smaller keyword:)")
  keyword=keyword.upper()
  keyword = ''.join(keyword.split()) 
  keyword ="".join(dict.fromkeys(keyword))
  dim1=keyword
  all_char=string.ascii_uppercase+string.digits+string.punctuation

  dim1=dim1+all_char
  dim1 ="".join(dict.fromkeys(dim1))
  #------------------------------
  # Τα εισάγει σε μία δισδιάστατη λίστα χωρίζοντάς το κείμενο σε ζευγάρια χαρακτήρων
  key_table = [dim1[y:y+8] for y in range(0,64,8)][:64]
  for x in range(64//8):
    print("-----------------------------")
    for j in range (7):
      if(j==0):
        print('| ' + key_table[x][j] +' |' , end=' ')
      elif (j<6):
        print(key_table[x][j] +' |' , end=' ')
      else :
        print(key_table[x][j] +' |' )
  print("-----------------------------")      
      
  print("Okay now that our array is ready it's time to decide what you want to do with it!")
  menu(key_table)


def menu(key_table):
  print('Pick something! For encryption enter A for decryption enter B. To stop the process now type q : ', end= ' ')
  while True:
      option = input().upper()
      if option != 'A' and option != 'B' and option !='Q':
          print("Sorry, I have no idea what to do with that:( Can you give me something that looks like these two : 'A' or 'B' or 'Q'?", end= ' ') 
          continue
      else:
          break
  if option == 'A' :
      print('Great! Time to encrypt a message:)')
      encryption(key_table)
      menu(key_table)

  elif option == 'B':
      print('Great! Time to decrypt a message:)') 
      decryption(key_table) 
      menu(key_table)
  else:
    exit()
table()
