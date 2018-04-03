from caesar import Caesar
#from affine import Affine
#Create a menu for the application.
c_list = ["CAESAR", "AFFINE", "SPAM", "EGGS"]

#def io_select(c_class):
#    while True:

#        ed_choice = input('Would you like to encrypt or decrypt a message? \n > ')
#        if ed_choice.upper() == 'ENCRYPT':
#            scramble = c_list[''].encrypt(input("What message would you like to encrypt? /> "))
#        elif ed_choice.upper() == 'DECRYPT':
#            unscramble = c_selection.decrypt(input("What should we decrypt? /> "))
            # Do other stuff. Return things.
#        else:
#            print("Please type either 'encrypt' or 'decrypt'")
#            continue


c_selection = input(
    """Greetings agent.
Please select your cipher.
--------
-Caesar-
--------
-Affine-
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
    #elif c_selection.upper() == c_list[2]:
    #    io_select(Spam())
    #elif c_selection.upper() == c_list[3]:
    #    io_select(Eggs())
else:
    print("""There is no {}. 
    Please choose from available ciphers.""".format(c_selection))
        # continue
