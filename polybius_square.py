import string

from ciphers import Cipher

class Polybius_square(Cipher):
    """The Polybius Square Cipher."""
    #ALPHANUM = string.ascii_uppercase + '0123456789'
    #ROWS = range(6)
    #COLS = range(6)
    #GRID = [(x, y) for y in ROWS for x in COLS]
    #AZ_NUMGRID = dict(zip(ALPHANUM, GRID))
    #NUM_AZ = dict([[valu,keey] for keey,valu in AZ_NUMGRID.items()])
    #AZ_NUMLIST = str(AZ_NUMGRID)
    #AZ_NUMLIST = AZ_NUMLIST.replace("), (", " ")
    #AZ_NUMLIST = AZ_NUMLIST.replace(", ", "")
    #AZ_NUMLIST = AZ_NUMLIST.replace("[(", "")
    #AZ_NUMLIST = AZ_NUMLIST.replace(")]", "")
    #print(AZ_NUMLIST)
    #print(AZ_NUMGRID)
    #print(NUM_AZ)

    def __init__(self):
        """Initializes instance of PS Cipher."""
        self.ALPHA = string.ascii_uppercase
        self.ALPHANUM = string.ascii_uppercase + '0123456789'
        self.ROWS = range(6)
        self.COLS = range(6)
        self.GRID = [(x, y) for y in self.ROWS for x in self.COLS]
        self.AZ_NUMGRID = dict(zip(self.ALPHANUM, self.GRID))
        self.NUM_AZ = dict([[valu,keey] for keey,valu in self.AZ_NUMGRID.items()])
        #AZ_NUMLIST = str(AZ_NUMGRID)
        #AZ_NUMLIST = AZ_NUMLIST.replace("), (", " ")
        #AZ_NUMLIST = AZ_NUMLIST.replace(", ", "")
        #AZ_NUMLIST = AZ_NUMLIST.replace("[(", "")
        #AZ_NUMLIST = AZ_NUMLIST.replace(")]", "")
    
    def encrypt(self, text):
        text = text.upper()
        output_string = ''
        poly_cip = []
        for char in text:
            try:
                poly_cip.append(self.AZ_NUMGRID[char])
            except KeyError:
                poly_cip.append(char)
                continue
        output_string = str(poly_cip)
        output_string = output_string.replace("), (", " ")
        output_string = output_string.replace(", ", "")
        output_string = output_string.replace("[(", "")
        output_string = output_string.replace(")]", "")
        output_string = output_string.replace(")'", "")
        output_string = output_string.replace("'(", "")
        return output_string
    
            
    
        #encrypt("CRYSTAL GEMS 1983")
    
    def decrypt(self, text):
        """Decrypts code.  Input must be all numbers."""
    
        #text = str(text)
        output_string = ''
        poly_cip = []
        #input_list = []
        output_list = []
        #for text[i] in text:
        #    input_list.append(int(text[i]))
        #print(input_list)
        #input_list.append(text.split())
        itera = len(text)
        while itera > 0:
            temp_tup = (int(text[0]), int(text[1]))
            # print(temp_tup)
            output_list.append(self.NUM_AZ[temp_tup])
            #output_list.extend(temp_tup)
            # print(output_list)
            text = text.replace(text[:2], '', 1)
            itera -= 2
    
        output = ''.join(output_list)
        return output
        
        #decrypt('2052040313005101400203')
