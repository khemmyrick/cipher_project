import string

from ciphers import Cipher


class Adfgvx(Cipher):
    """The ADFGVX Cipher."""
    
    def __init__(self):
        self.ALPHANUM = string.ascii_uppercase + '0123456789'
        self.ROWS = ['A', 'D', 'F', 'G', 'V', 'X']
        self.COLS = ['A', 'D', 'F', 'G', 'V', 'X']
        self.GRID = [(x, y) for y in self.ROWS for x in self.COLS]
        self.AZ_NUMGRID = dict(zip(self.ALPHANUM, self.GRID))
        self.NUM_AZ = dict([[valu, keey] for keey, valu in self.AZ_NUMGRID.items()])
        # print(ALPHANUM)

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
        output_string = output_string.replace("'", "")
        return output_string    

    def decrypt(self, text):
        """Decrypts code.  Input must be all letters."""
        output_list = []
        text = text.upper()
        itera = len(text)

        while itera > 0:
            temp_tup = (text[0], text[1])
            output_list.append(self.NUM_AZ[temp_tup])
            text = text.replace(text[:2], '', 1)
            itera -= 2

        output = ''.join(output_list)
        return output
