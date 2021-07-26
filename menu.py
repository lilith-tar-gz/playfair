print('Welcome to our playfair calculator!')
print("Let's create our array! Think of a keyword. Enter the letters of the word in UPPERCASE without repeating them. Fill the rest of the array with the letters of the alphabet alphabetically skipping J and the letters you've already used ")
key_table = [[0 for i in range(5)] for j in range(5)] 
for i in range(5):
    for j in range(5):
        key_table[i][j]=input("Enter letter : ")
print("Okay now that our array is ready it's time to decide what you want to do with it!")
while True:
    option = input('Pick something! For encryption enter A for decryption enter B : ')
    if option != 'A' and option != 'B':
        print("Sorry, I have no idea what to do with that:( Can you give me something that looks like these 2? (A or B) ")
        continue
    else:
        break
if option == 'A' :
    print('Great! Time to encrypt a message:)')
else :
    print('Great! Time to decrypt a message:)')   
