import string



ALPHANUM = string.ascii_uppercase + '0123456789'
rows = range(6)
cols = range(6)
GRID = [(x, y) for y in rows for x in cols]
AZ_NUMGRID = dict(zip(ALPHANUM, GRID))
#print(AZ_NUMGRID)

def encrypt(text):
    output_string = ''
    poly_cip = []
    polyanna = []
    for char in text:
        poly_cip.append(AZ_NUMGRID[char])
    output_string = str(poly_cip)
    output_string = output_string.replace("), (", " ")
    output_string = output_string.replace(", ", "")
    output_string = output_string.replace("[(", "")
    output_string = output_string.replace(")]", "")
    print(output_string)

encrypt("AQUADRY")
#from ciphers import Cipher

#class Polybius_square(Cipher):
#    """The Polybius Square Cipher."""
#    ALPHANUM = string.ascii_uppercase + '0123456789'
#    rows = list(range(6))
#    cols = list(range(6))
#    GRID = [(x, y) for y in rows for x in cols]
#    AZ_NUMGRID = dict(zip(ALPHANUM, GRID))

#    def __init__(self):
#        """Initializes instance of Affine Cipher."""
#        self.AZ_NUMGRID = dict(zip(AZ_NUM, GRID))

#    def encrypt(self, text):
#        output_string = ''
#        poly_cip = ''
#        for char in text:
#            poly_cip += self.AZ_NUMGRID[char]
        # output_string = str(poly_cip)
#        return output_string
        
#    def decrypt(self, text):
#        pass
        


#p_square = {letter:(col, row) for row in rows for col in cols for letter in ALPHANUM}

#print(p_square)