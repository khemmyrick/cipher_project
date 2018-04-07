import string

from ciphers import Cipher


class Atbash(Cipher):
    """The Atbash Cipher."""
    ALPHA = string.ascii_uppercase
    REV_ALPHA = ALPHA[::-1]

    def __init__(self):
        """Initializes instance of Atbash Cipher."""
        self.ALPHA = string.ascii_uppercase

    def encrypt(self, text):
        """Encrypt a string, via instance.encrypt(string)."""
        output_string = ""
        text = text.upper()
        for char in text:
            try:
                output_string += self.REV_ALPHA[self.ALPHA.index(char)]
            except ValueError:
                output_string += char
        return output_string

    def decrypt(self, text):
        """Decrypt a string, via instance.decrypt(string)."""
        output_string = ""
        text = text.upper()
        for char in text:
            try:
                output_string += self.ALPHA[self.REV_ALPHA.index(char)]
            except ValueError:
                output_string += char
        return output_string
