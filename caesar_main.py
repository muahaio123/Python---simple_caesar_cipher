print('''                                      _       _               
                                     (_)     | |              
  ___ __ _  ___  ___  ___ _ __    ___ _ _ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _ \ '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \  __/ |    | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\___|_|     \___|_| .__/|_| |_|\___|_|   
                                       | |                    
                                       |_|                    ''')

def caesar(mesg, shift, mod):
    new_mssg = ''
    
    if mod == 'decode':
        shift *= -1
        
    for ch in mesg:
        if ch not in alphabet:
            new_mssg += ch
        else:
            new_mssg += alphabet[(alphabet.index(ch) + shift) % 26]
            
    print(new_mssg)

alphabet = ('a b c d e f g h i j k l m n o p q r s t u v w x y z').split()

again = 'y'
while again == 'y':
    mode = input("\nType 'encode' to encrypt, or 'decode' to decrypt a message: ")
    message = input("Please type the message: ").lower()
    shift_amount = int(input("Please type the shift number: "))

    caesar(mesg = message, shift = shift_amount, mod = mode)

    again = input("Type 'y' if you want to go again | otherwise to exit: ").lower()
