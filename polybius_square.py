import string


ALPHANUM = string.ascii_uppercase + '0123456789'
rows = range(6)
cols = range(6)
GRID = [(x, y) for y in rows for x in cols]
AZ_NUMGRID = dict(zip(ALPHANUM, GRID))
NUM_AZ = dict([[valu,keey] for keey,valu in AZ_NUMGRID.items()])
AZ_NUMLIST = str(AZ_NUMGRID)
AZ_NUMLIST = AZ_NUMLIST.replace("), (", " ")
AZ_NUMLIST = AZ_NUMLIST.replace(", ", "")
AZ_NUMLIST = AZ_NUMLIST.replace("[(", "")
AZ_NUMLIST = AZ_NUMLIST.replace(")]", "")
#print(AZ_NUMLIST)
#print(AZ_NUMGRID)
#print(NUM_AZ)

def encrypt(text):
    print(text)
    output_string = ''
    poly_cip = []
    for char in text:
        try:
            poly_cip.append(AZ_NUMGRID[char])
        except KeyError:
            if char == " ":
                poly_cip.append("  ") 
            else:
                poly_cip.append(char)
            continue
    output_string = str(poly_cip)
    output_string = output_string.replace("), (", " ")
    output_string = output_string.replace(", ", "")
    output_string = output_string.replace("[(", "")
    output_string = output_string.replace(")]", "")
    output_string = output_string.replace(")'", "")
    output_string = output_string.replace("'(", "")
    print(output_string)

        

encrypt("CRYSTAL GEMS")

def decrypt(text):
    """Decrypts code.  Input must be all numbers."""

    #text = str(text)
    output_string = ''
    poly_cip = []
    input_list = []
    output_list = []
    #for text[i] in text:
    #    input_list.append(int(text[i]))
    #print(input_list)
    input_list.append(text.split())
    itera = len(text)
    while itera > 0:
        temp_tup = (int(text[0]), int(text[1]))
        # print(temp_tup)
        output_list.append(NUM_AZ[temp_tup])
        #output_list.extend(temp_tup)
        # print(output_list)
        text = text.replace(text[:2], '', 1)
        itera -= 2

    output = ''.join(output_list)
    print(output)
    
decrypt('00422300305204')
    #for pair in input_list:
    #    [k for (k, v) in AZ_NUMGRID.iteritems() if v == 0]

    #for char in text:
    #    poly_cip.append(AZ_NUMGRID[char])
    #output_string = str(poly_cip)
    #output_string = output_string.replace("), (", " ")
    #output_string = output_string.replace(", ", "")
    #output_string = output_string.replace("[(", "")
    #output_string = output_string.replace(")]", "")
    #print(output_string)    

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