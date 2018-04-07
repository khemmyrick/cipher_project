import os

from caesar import Caesar
from affine import Affine
from atbash import Atbash
from polybius_square import Polybius_square

c_list = ["CAESAR", "AFFINE", "ATBASH", "POLYBIUS SQUARE", "SPAM"]


def encrypt_message(session):
    message = input("What message would you like to encrypt? > ")
    print(session.encrypt(message))


def decrypt_message(session):
    message = input("What message would you like to decrypt? > ")
    print(session.decrypt(message))


def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def press_start():
    start = input("Greetings agent. Do you have a message? y/n > ")
    if start == "y":
        clear_screen()
        secrets()
    else:
        quit()


def restart():
    again = input("Encrypt or decrypt another message? y/n > ")
    if again == "y":
        clear_screen()
        secrets()
    else:
        quit()


def secrets():
    c_selection = input(
        """Excellent.
    Please select your cipher.
    -----------------
    -----Caesar------
    -----------------
    -----Affine------
    -----------------
    -----Atbash------
    -----------------
    -Polybius Square-
    -----------------
    > """)
    clear_screen()
    print(c_selection.upper() + ":")

    if c_selection.upper() in c_list:
        if c_selection.upper() == c_list[0]:
            print("The emperor of ciphers.")
            session = Caesar()
            ende = input("Would you like to encrypt or decrypt? > ")
            if ende.lower() == 'encrypt':
                encrypt_message(session)
                restart()
            elif ende.lower() == 'decrypt':
                decrypt_message(session)
                restart()
        elif c_selection.upper() == c_list[1]:
            print("A very fine cipher indeed!")
            session = Affine()
            ende = input("Would you like to encrypt or decrypt? > ")
            if ende.lower() == 'encrypt':
                key_a = input("""Please record the two keys you use to get this code.
For the first key, please choose an integer from the following:
    3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 > """)
                key_b = input("Please choose any integer for second key. > ")
                message = input("What message would you like to encrypt? > ")
                print(session.encrypt(message, int(key_a), int(key_b)))
                restart()
            elif ende.lower() == 'decrypt':
                key_a = input("Please insert the first key number. > ")
                key_b = input("Please insert the second key number. > ")
                message = input("What message would you like to decrypt? > ")
                print(session.decrypt(message, int(key_a), int(key_b)))
                restart()
        elif c_selection.upper() == c_list[2]:
            print("For minimum security messages only.")
            session = Atbash()
            ende = input("Would you like to encrypt or decrypt? > ")
            if ende.lower() == 'encrypt':
                encrypt_message(session)
                restart()
            elif ende.lower() == 'decrypt':
                decrypt_message(session)
                restart()
        elif c_selection.upper() == c_list[3]:
            print("Sharp on all four corners.")
            session = Polybius_square()
            ende = input("Would you like to encrypt or decrypt? > ")
            if ende.lower() == 'encrypt':
                message = input("Please insert message. "
                                "(Letters and numbers only please.) > ")
                print(session.encrypt(message))
                restart()
            elif ende.lower() == 'decrypt':
                message = input("Please enter code. Numbers only. No spaces.")
                print(session.decrypt(str(message)))
                restart()
        # else:
    else:
        print("""There is no {}.
        Please choose from available ciphers.""".format(c_selection))
        restart()


press_start()
