# Κρυπτογράφηση
def encryption(key_table):
    #----------------------------------------------------------------------------   
    #Ζητάει από τον χρήστη να εισάγει το κείμενο που θέλει να κρυπτογραφίσει 
    message = input("Enter the message you want to encrypt in UPPERCASE. !REMEMBER! : Use only ONE space character to seperate words ")
    #Αφού κάνει τις απαιτούμενες αλλαγές : 
    #1) Αφαιρεί τους κενούς χαρακτήρες του κειμένου και μετατρέπει τους χαρακτήρες σε κεφαλαία
    message = ''.join(message.split()) 
    message = message.upper()

    #2) Αντικαθιστεί τον χαρακτήρα J με τον χαρακτήρα I
    message = message.replace("J" , "I")

    #3) Προσθέτει τον χαρακτήρα Q ανάμεσα σε διπλανούς όμοιους χαρακτήρες
    cnumber = len(message)
    for x in range(cnumber-1): 
        if message[x] == message[x+1]:
            message = message[:x+1] + 'Q' +message[x+1:]
            cnumber += 1
    chain = list(message)

    #4) Εισάγει τον χαρακτήρα Q στο τέλος του νήματος αν ο αριθμός των χαρακτήρων είναι μονός
    if cnumber % 2 == 1:
        chain.append('Q') 
        cnumber +=1

    # Τα εισάγει σε μία δισδιάστατη λίστα χωρίζοντάς το κείμενο σε ζευγάρια χαρακτήρων
    new_chain = [chain[y:y+2] for y in range(0,cnumber,2)][:cnumber]

    #1) Αναζητά τις θέσεις των ζευγαριών της λίστας στον πίνακα με τη λέξη κλειδί
    for r in range(0,cnumber//2,1):
        i1 = -1
        i2 = -1
        j1 = -1
        j2 = -1
        key1 = new_chain[r][0]
        key2 = new_chain[r][1]
        found1 = False
        found2 = False
        for i in range(8) : 
            for j in range(8) :
                if key1 == key_table[i][j] :
                    i1 = i
                    j1 = j
                    found1 = True
                if key2 == key_table[i][j] :
                    i2 = i
                    j2 = j
                    found2 = True
                if found1 and found2 :
                    break
            if found1 and found2 :
                break
        if i1 == i2 :
            if j1 == 7 :
                new_chain[r][0] = key_table[i1][0]
                new_chain[r][1] = key_table[i2][j2+1]
            elif j2 == 7 :
                new_chain[r][0] = key_table[i1][j1+1]
                new_chain[r][1] = key_table[i2][0]    
            else :
                new_chain[r][0] = key_table[i1][j1+1]
                new_chain[r][1] = key_table[i2][j2+1]
        elif j1 == j2 :
            if i1 == 7 :
                new_chain[r][0] = key_table[0][j1]
                new_chain[r][1] = key_table[i2+1][j2]
            elif i2 == 7 :
                new_chain[r][0] = key_table[i1+1][j1]
                new_chain[r][1] = key_table[0][j2] 
            else : 
                new_chain[r][0] = key_table[i1+1][j1]
                new_chain[r][1] = key_table[i2+1][j2]
        else :
            new_chain[r][0] = key_table[i1][j2]
            new_chain[r][1] = key_table[i2][j1]

    print("This is the final message : ")
    for i in range(cnumber//2):
        for j in range(2):
            print(new_chain[i][j], end="")
    print("\n")
  
#         _____  
#       /  ___  \
#     /  /  _  \  \
#   /( /( /(_)\ )\ )\
#  (  \  \ ___ /  /  )
#  (    \ _____ /    )
#  /(               )\
# |  \             /  |
# |    \ _______ /    |
#  \    / \   / \    /
#    \/    | |    \/
#          | | 
#          | |
#          | |

#          this is for you <3