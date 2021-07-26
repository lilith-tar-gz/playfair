#----------------------------------------------------------------------------   
key_table = [['P', 'L', 'A', 'Y', 'F'], ['I', 'R', 'B', 'C', 'D'], ['E', 'G', 'H', 'K', 'M'], ['N', 'O', 'Q', 'S', 'T'], ['U', 'V', 'W', 'X', 'Z']]
# # Αποκρυπτογράφηση
# Ζητάει από τον χρήστη να εισάγει το κείμενο που θέλει να αποκρυπτογραφίσει 
hidden_message = input("Enter the crypted message you've been sent without using space characters : ")

# Αφού κάνει τις απαιτούμενες αλλαγές :
# Αφαιρεί τους κενούς χαρακτήρες του κειμένου και μετατρέπει τους χαρακτήρες σε κεφαλαία
hidden_message = ''.join(hidden_message.split()) 
hidden_message = hidden_message.upper()
# Δημιουργεί μια λίστα με τους χαρακτήρες 
hidden_chain = list(hidden_message)
# print("length hidden_message: ", len(hidden_message))
hidden_cnumber = len(hidden_message)
# Δημιουργεί μία δισδιάστατη λίστα χωρίζοντάς το κείμενο σε ζευγάρια χαρακτήρων
hidden_new_chain = [hidden_chain[y:y+2] for y in range(0,hidden_cnumber,2)][:hidden_cnumber]
for r in range(0,hidden_cnumber//2,1):
    i1 = -1
    i2 = -1
    j1 = -1
    j2 = -1
    key1 = hidden_new_chain[r][0]
    key2 = hidden_new_chain[r][1]
    found1 = False
    found2 = False
    # print("key1: ",key1)
    # print("key2: ",key2)

    for i in range(5) : 
        for j in range(5) :
            if key1 == key_table[i][j] :
                i1 = i
                j1 = j
                found1 = True
                # print("key1: ", key1)
                # print("key_table[i][j]: ", key_table[i][j])
                # print("in first if" , key_table[i1][j1])
            if key2 == key_table[i][j] :
                i2 = i
                j2 = j
                found2 = True
                # print("key2: ", key2)
                # print("key_table[i][j]: ", key_table[i][j])
                # print("in second if" , key_table[i2][j2])
            if found1 and found2 :
                break
            # print("i: ",i,"j: ",j)
        if found1 and found2 :
            break
        
    # print(" Found the characters in those positions : [" , i1 , ", " , j1 , "] and [", i2 , ", " , j2 , "]" )
    # print("") #gia new line    
    
    if i1 == i2 :
        if j1 == 0 :
            hidden_new_chain[r][0] = key_table[i1][4]
            hidden_new_chain[r][1] = key_table[i2][j2-1]
        elif j2 == 0 :
            hidden_new_chain[r][0] = key_table[i1][j1-1]
            hidden_new_chain[r][1] = key_table[i2][4]    
        else :
            hidden_new_chain[r][0] = key_table[i1][j1-1]
            hidden_new_chain[r][1] = key_table[i2][j2-1]
    elif j1 == j2 :
        if i1 == 0 :
            hidden_new_chain[r][0] = key_table[4][j1]
            hidden_new_chain[r][1] = key_table[i2-1][j2]
        elif i2 == 0 :
            hidden_new_chain[r][0] = key_table[i1-1][j1]
            hidden_new_chain[r][1] = key_table[4][j2] 
        else : 
            hidden_new_chain[r][0] = key_table[i1-1][j1]
            hidden_new_chain[r][1] = key_table[i2-1][j2]
    else :
        hidden_new_chain[r][0] = key_table[i1][j2]
        hidden_new_chain[r][1] = key_table[i2][j1]
hidden_new_message = ""
for i in range(hidden_cnumber//2) :
    for j in range(2) :
        hidden_new_message += hidden_new_chain[i][j]
  
# print("hidden_new_message before removal: ", hidden_new_message)
# print("hidden_new_message length: ", len(hidden_new_message))
# print("hidden cnumber: ",hidden_cnumber)

# for x in range(1, hidden_cnumber-2) :
for x in range(1, len(hidden_new_message)-2) :
    # print("x: " , x)
    if hidden_new_message[x-1] == hidden_new_message[x+1] and hidden_new_message[x] == "Q" :
        # print("found x letter is: " , hidden_new_message[x])
        hidden_new_message = hidden_new_message[:x] + hidden_new_message[x+1:]
    # print("NEW hidden_new_message length: ", len(hidden_new_message)) 
        
# print("new hidden_new_message length: ", len(hidden_new_message))
# if  hidden_new_message[hidden_cnumber-1] == "Q" :
if  hidden_new_message[len(hidden_new_message)-1] == "Q" :
    hidden_new_message = hidden_new_message[:-1]
print(hidden_new_message)



