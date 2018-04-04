import string

from ciphers import Cipher

# alphanum = string.ascii_uppercase + '0123456789'
# If we add numbers to this cipher, does it still count as an Atbash?
# revalphanum = alphanum[::-1]

class Atbash(Cipher):
    """The Atbash Cipher."""
    # alpha = string.ascii_uppercase
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
            output_string += self.REV_ALPHA[self.ALPHA.index(char)]

        return output_string

    
    def decrypt(self, text):
        """Decrypt a string, via instance.decrypt(string)."""
        output_string = ""
        text = text.upper()
        for char in text:
            output_string += self.ALPHA[self.REV_ALPHA.index(char)]

        return output_string        
