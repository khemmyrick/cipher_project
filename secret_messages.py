import os

from caesar import Caesar
from affine import Affine
from atbash import Atbash
from polybius_square import PolybiusSquare


c_list = [
    "CAESAR",
    "AFFINE",
    "ATBASH",
    "POLYBIUS SQUARE",
    "1",
    "2",
    "3",
    "4"
]

affine_list = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def press_start():
    """Start the app."""
    start = input("Greetings agent. Do you have a message? Y/n > ")
    if start == "n":
        quit()
    else:
        clear_screen()
        secrets()


def restart():
    """Restart the app."""
    again = input("Encrypt or decrypt another message? Y/n > ")
    if again.lower() == "n":
        quit()
    else:
        clear_screen()
        secrets()


def encrypt_message(session):
    """Encrypt a messsage."""
    message = input("What message would you like to encrypt? \n"
                    "(Warning: Non-letters will not be encoded!) > ")
    print(session.encrypt(message))


def decrypt_message(session):
    """Decrypt a message."""
    message = input("What message would you like to decrypt? > ")
    print(session.decrypt(message))


def affine_session(session, ende):
    """Encrypt or decrypt a message using Affine Cipher."""
    while True:
        key_a = input("""Select the first of 2 keys, from the following:
        3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 > """)
        try:
            if int(key_a) in affine_list:
                key_b = input("Please choose any integer for second key. > ")
                try:
                    b_num = int(key_b)
                    if ende == 'encrypt':
                        message = input("What would you like to encrypt? > ")
                        message = message.replace(' ', '')
                        print(session.encrypt(message, int(key_a), b_num))
                        return
                    else:
                        message = input("What would you like to decrypt? > ")
                        message = message.replace(' ', '')
                        print(session.decrypt(message, int(key_a), b_num))
                        return
                except ValueError:
                    print("Both keys must be integers.")
                    continue
                except KeyError:
                    print("Letters only, please.")
                    continue
                else:
                    continue
            else:
                print("First key number must be chosen from the list.")
                continue
        except ValueError:
            print("First key number must be chosen from the list.")
            continue


def polys_encrypt(session):
    """Encrypt a message using Polybius Square Cipher."""
    message = input("Please insert message to encrypt. "
                    "Only letters/numbers will be encrypted. > ")
    print(session.encrypt(message))


def polys_decrypt(session):
    """Decrypt a message using Polybius Square Cipher."""
    message = input("Please enter code. Numbers 0 through 5 only."
                    "No spaces. > ")
    print(session.decrypt(str(message)))


def cipher_select(ende):
    """Select the cipher."""
    c_selection = input(
        """Excellent.
    Please select your cipher by name or number.
    -------------------------
    ---[1]----Caesar---------
    -------------------------
    ---[2]----Affine---------
    -------------------------
    ---[3]----Atbash---------
    -------------------------
    ---[4]-Polybius Square---
    -------------------------
    > """)
    clear_screen()

    if c_selection.upper() in c_list:
        if c_selection.upper() == c_list[0] or c_selection == "1":
            print("CAESAR: \n The emperor of ciphers.")
            session = Caesar()
            if ende == 'encrypt':
                encrypt_message(session)
                restart()
            elif ende == 'decrypt':
                decrypt_message(session)
                restart()
        elif c_selection.upper() == c_list[1] or c_selection == "2":
            print("AFFINE: \n A very fine cipher indeed!")
            session = Affine()
            affine_session(session, ende)
            restart()
        elif c_selection.upper() == c_list[2] or c_selection == "3":
            print("ATBASH: \n For minimum security messages only.")
            session = Atbash()
            if ende == 'encrypt':
                encrypt_message(session)
                restart()
            elif ende == 'decrypt':
                decrypt_message(session)
                restart()
        elif c_selection.upper() == c_list[3] or c_selection == "4":
            print("POLYBIUS SQUARE: \n Sharp on all four corners.")
            session = PolybiusSquare()
            if ende == 'encrypt':
                polys_encrypt(session)
                restart()
            elif ende == 'decrypt':
                polys_decrypt(session)
                restart()
    else:
        print("""There is no {}.
        Please choose from available ciphers.""".format(c_selection))
        restart()


def secrets():
    """Ask if user wants to encrypt or decrypt."""
    ende = input("What would you like to do? \n"
                 "Type 'E' or 'ENCRYPT' for encrypt(default setting). \n"
                 "Type 'D' or 'DECRYPT' for decrypt. \n"
                 "> ")
    if ende.lower() == 'd' or ende.lower() == 'decrypt':
        ende = 'decrypt'
    else:
        ende = 'encrypt'
    cipher_select(ende)

press_start()
