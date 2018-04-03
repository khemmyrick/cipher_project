import string

from ciphers import Cipher

class Affine(Cipher):
    """The Affine Cipher."""
    # alpha = string.ascii_uppercase
    ALPHA = string.ascii_uppercase
    
    def __init__(self):
        """Initializes instance of Affine Cipher."""
#        self.key_a = key_a
#        self.key_b = key_b
        self.ALPHA = string.ascii_uppercase
        
    def encrypt(self, text, key_a, key_b):
        """Encrypt a string, via instance.encrypt(string)."""
        affine_cip = ""
        output_string = ""
        text = text.upper()
        for char in self.ALPHA:
            affine_cip += (self.ALPHA[(key_a * self.ALPHA.index(char) + key_b) % 26])
        alpha_dict = {letter: number for number, letter in zip(range(0,26), self.ALPHA)}
        affine_dict = {number: letter for letter, number in zip(affine_cip, range(0,26))}
        for char in text:
            output_string += affine_dict[alpha_dict[char]]

        return output_string

    
    def decrypt(self, text, key_a, key_b):
        """Decrypt a string, via instance.decrypt(string)."""
        affine_cip = ""
        output_string = ""
        text = text.upper()
        for char in self.ALPHA:
            affine_cip += (self.ALPHA[(key_a * self.ALPHA.index(char) + key_b) % 26])
        rev_affine_dict = {number: letter for letter, number in zip(range(0,26), affine_cip)}
        rev_alpha_dict = {letter: number for number, letter in zip(self.ALPHA, range(0,26))}
        for char in text:
            output_string += rev_alpha_dict[rev_affine_dict[char]]            
        return output_string
        
        # input_string = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
# output_string = ""
# affine_num = []
# key_a = 5
# key_b = 8

# alpha = string.ascii_uppercase
# affine_cip = ""
# for char in alpha:
#    affine_cip += (alpha[(key_a * alpha.index(char) + key_b) % 26])

# Compare each letter in input string to each letter in full alphabet,
# Return corresponding letter in cipher.
    
# print(input_string)
# input_string -> alpha_index [int list] -> cipher_index [int list] -> output_string
# alpha_dict = {letter: number for number, letter in zip(range(0,26), alpha)}

# affine_dict = {number: letter for letter, number in zip(affine_cip, range(0,26))}

# for char in input_string:
#    output_string += affine_dict[alpha_dict[char]]
    
# print(output_string)

# new_output = ""
# rev_affine_dict = {number: letter for letter, number in zip(range(0,26), affine_cip)}

# rev_alpha_dict = {letter: number for number, letter in zip(alpha, range(0,26))}


# for char in output_string:
#    new_output += rev_alpha_dict[rev_affine_dict[char]]
    
# print(new_output)
