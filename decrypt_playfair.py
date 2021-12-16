# Αποκρυπτογράφηση

def decryption(key_table):
    #---------------------------------------------------------------------------- 
    # Ζητάει από τον χρήστη να εισάγει το κείμενο που θέλει να αποκρυπτογραφίσει 
    hidden_message = input("Enter the crypted message you've been sent without using space characters : ")
    # Αφού κάνει τις απαιτούμενες αλλαγές :
    # Αφαιρεί τους κενούς χαρακτήρες του κειμένου και μετατρέπει τους χαρακτήρες σε κεφαλαία
    hidden_message = ''.join(hidden_message.split()) 
    hidden_message = hidden_message.upper()
    # Δημιουργεί μια λίστα με τους χαρακτήρες 
    hidden_chain = list(hidden_message)
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
            if j1 == 0 :
                hidden_new_chain[r][0] = key_table[i1][7]
                hidden_new_chain[r][1] = key_table[i2][j2-1]
            elif j2 == 0 :
                hidden_new_chain[r][0] = key_table[i1][j1-1]
                hidden_new_chain[r][1] = key_table[i2][7]    
            else :
                hidden_new_chain[r][0] = key_table[i1][j1-1]
                hidden_new_chain[r][1] = key_table[i2][j2-1]
        elif j1 == j2 :
            if i1 == 0 :
                hidden_new_chain[r][0] = key_table[7][j1]
                hidden_new_chain[r][1] = key_table[i2-1][j2]
            elif i2 == 0 :
                hidden_new_chain[r][0] = key_table[i1-1][j1]
                hidden_new_chain[r][1] = key_table[7][j2] 
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
    for x in range(1, len(hidden_new_message)-2) :
        if hidden_new_message[x-1] == hidden_new_message[x+1] and hidden_new_message[x] == "Q" :
            hidden_new_message = hidden_new_message[:x] + hidden_new_message[x+1:]
    if  hidden_new_message[len(hidden_new_message)-1] == "Q" :
        hidden_new_message = hidden_new_message[:-1]
    print(hidden_new_message)
    


