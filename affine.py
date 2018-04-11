import string

from ciphers import Cipher


class Affine(Cipher):
    """The Affine Cipher."""
    ALPHA = string.ascii_uppercase

    def __init__(self):
        """Initializes instance of Affine Cipher."""
        self.ALPHA = string.ascii_uppercase

    def encrypt(self, text, key_a, key_b):
        """Encrypt a string, via instance.encrypt(string)."""
        # wikipedia's affine example puts key_a as 5 and key_b as 8.
        # work try except script in to ensure key_a is valid
        # and make sure affine cipher can deal with non-letters.
        affine_cip = ""
        output_string = ""
        text = text.upper()
        for char in self.ALPHA:
            affine_cip += (self.ALPHA[(key_a *
                                       self.ALPHA.index(char) +
                                       key_b) % 26])
        alpha_dict = {letter: number
                      for number, letter in zip(range(0, 26), self.ALPHA)}
        affine_dict = {number: letter
                       for letter, number in zip(affine_cip, range(0, 26))}
        for char in text:
            output_string += affine_dict[alpha_dict[char]]

        return output_string

    def decrypt(self, text, key_a, key_b):
        """Decrypt a string, via instance.decrypt(string)."""
        affine_cip = ""
        output_string = ""
        text = text.upper()
        for char in self.ALPHA:
            affine_cip += (self.ALPHA[(key_a *
                                       self.ALPHA.index(char) +
                                       key_b) % 26])
        rev_affine_dict = {number: letter
                           for letter, number in zip(range(0, 26), affine_cip)}
        rev_alpha_dict = {letter: number
                          for number, letter in zip(self.ALPHA, range(0, 26))}
        for char in text:
            output_string += rev_alpha_dict[rev_affine_dict[char]]
        return output_string
