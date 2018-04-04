from caesar import Caesar
from affine import Affine
from atbash import Atbash
# Create a menu for the application.
c_list = ["CAESAR", "AFFINE", "ATBASH", "SPAM"]

c_selection = input(
    """Greetings agent.
Please select your cipher.
--------
-Caesar-
--------
-Affine-
--------
-Atbash-
--------
> """)

print(c_selection.upper() + ":")

if c_selection.upper() in c_list:
    if c_selection.upper() == c_list[0]:
        print("The emperor of ciphers.")
        session = Caesar()
        ende = input("Would you like to encrypt or decrypt? > ")
        if ende.lower() == 'encrypt':
            message = input("What message would you like to encrypt? > ")
            print(session.encrypt(message))
        elif ende.lower() == 'decrypt':
            message = input("What message would you like to decrypt? > ")
            print(session.decrypt(message))
    elif c_selection.upper() == c_list[1]:
        print("A very fine cipher indeed!")
        session = Affine()
        ende = input("Would you like to encrypt or decrypt? > ")
        if ende.lower() == 'encrypt':
            key_a = input("""For the first key, please choose an integer from the following:
            3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25""")
    elif c_selection.upper() == c_list[2]:
        print("For minimum security messages only.")
        session = Atbash()
        ende = input("Would you like to encrypt or decrypt? > ")
        if ende.lower() == 'encrypt':
            message = input("What message would you like to encrypt?")
            print(session.encrypt(message))
        elif ende.lower() == 'decrypt':
            message = input("What message would you like to decrypt?")
            print(session.decrypt(message))
        # else:
            
    #elif c_selection.upper() == c_list[2]:
    #    io_select(Spam())
    #elif c_selection.upper() == c_list[3]:
    #    io_select(Eggs())
else:
    print("""There is no {}. 
    Please choose from available ciphers.""".format(c_selection))
        # continue
