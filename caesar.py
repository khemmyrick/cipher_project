import string

from ciphers import Cipher


class Caesar(Cipher):
    """The Caesar Cipher."""
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        """Initializes an instance of the Caesar cipher.
        This instance can be fed a string to encrypt.
        And this same instance (or any instance of Caesar cipher)
        can be used to decrypt said strings.
        """
        self.offset = offset
        # Sets instance.offset to offset argument, in this case, "3".
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        """Encrypt a string, via instance.encrypt(string)."""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        """Decrypt a string."""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
