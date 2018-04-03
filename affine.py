import string

input_string = "PALACE"
output_string = ""
affine_num = []
key_a = 5
key_b = 8

alpha = string.ascii_uppercase
affine_cip = ""
for char in alpha:
    affine_cip += (alpha[(key_a * alpha.index(char) + key_b) % 26])

# Compare each letter in input string to each letter in full alphabet,
# Return corresponding letter in cipher.
    
print(input_string)
alpha_dict = {letter: number for number, letter in zip(range(0,26), alpha)}

affine_dict = {number: letter for letter, number in zip(affine_cip, range(0,26))}

for char in input_string:
    output_string += affine_dict[alpha_dict[char]]
    
print(output_string)
#affine_num.append
#for char in alpha_list:
#    if char in alpha:
#        affine_num.append(alpha.index(char))

#print(affine_num)

# input_string -> alpha_index [int list] -> cipher_index [int list] -> output_string






#affine_num += str
#print(alpha.index(char for char in input_string))
#print(affine_num)
#output_string += affine_cip[num for num in affine_num]


#print(output_string)
#class Affine(Cipher):
#    """The Affine Cipher."""
#    FORWARD = string.ascii_uppercase
    # Sets variable FORWARD to 3 sets of entire all-caps alphabet.

#    def __init__(self, key_a, key_b):
#        """Initializes an instance of the Affine cipher.
#        This instance can be fed a string to encrypt.
#        And this same instance (or any instance of Caesar cipher)
#        can be used to decrypt said strings.
#        """
#        self.key_a = key_a
#        self.key_b = key_b
        # Sets instance.offset to offset argument, in this case, "3".
        
#        for i in range(26):

#            self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]



        # Sets instance.FORWARD to all-caps alphabet (plus alpha to offset (which is 3) plus 1).
#        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase
        # Sets instance.BACKWARD to an all caps offset + 1, plus full alphabet.

#####
#def affine(a, b):
#    for i in range(26):
        #transpo_table = {chr(i+65): chr(((a*i+b)%26)+65)}
#        print({string.ascii_uppercase: (a * string.ascii_uppercase * b)%26})
        #print(transpo_table)

#An example call
#affine(5, 8)



# from ciphers import Cipher
# Implement 3 ciphers.  Each with its own class and module.
# Docstrings for all functions/methods.
#class Affine(Cipher):
#    """The Affine Cipher."""
    # *** for demonstration purposes, from wikipedia page on affine cipher.
    #Prints a transposition table for an affine cipher.
    #a must be coprime to m=26.
    # if we add 0 - 9 to cipher, m will be 36.
    # key_a can never be any even integer or 13 with an m of 26.
    # for an m=36, key_a can  never be any even integer or 3.
#    def __init__(self, key_a, key_b):
        # a and b are the key of the cipher.
        # key_b can be anything, as long as key_a isn't 1.

#        for i in range(m=26):
            #if (key_a * (key_a ^ -1)) % m == 1:
#            return(chr(i+65) + ": " + chr(((key_a*i+key_b)%26)+65))

#An example call
#affine(5, 8)

# *** end wikipedia code.

