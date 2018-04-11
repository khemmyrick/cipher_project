import string

from ciphers import Cipher


class PolybiusSquare(Cipher):
    """The Polybius Square Cipher."""

    def __init__(self):
        """Initializes instance of PS Cipher."""
        self.ALPHA = string.ascii_uppercase
        self.ALPHANUM = string.ascii_uppercase + '0123456789'
        self.ROWS = range(6)
        self.COLS = range(6)
        self.GRID = [(x, y) for y in self.ROWS for x in self.COLS]
        self.AZ_NUMGRID = dict(zip(self.ALPHANUM, self.GRID))
        self.NUM_AZ = dict([[valu, keey]
                            for keey, valu in self.AZ_NUMGRID.items()])

    def encrypt(self, text):
        text = text.upper()
        output_string = ''
        poly_cip = []
        for char in text:
            try:
                poly_cip.append(self.AZ_NUMGRID[char])
            except KeyError:
                text = text.replace(char, '')
                continue
        output_string = str(poly_cip)
        output_string = output_string.replace("), (", " ")
        output_string = output_string.replace(", ", "")
        output_string = output_string.replace("[(", "")
        output_string = output_string.replace(")]", "")
        output_string = output_string.replace(")'", "")
        output_string = output_string.replace("'(", "")
        return output_string

    def decrypt(self, text):
        """Decrypts code.  Input must be all numbers."""
        output_list = []
        itera = len(text)

        while itera > 0:
            oops = False
            try:
                temp_tup = (int(text[0]), int(text[1]))
                output_list.append(self.NUM_AZ[temp_tup])
                text = text.replace(text[:2], '', 1)
                itera -= 2
            except ValueError:
                print("Error: Expected integer(s), got non-integer(s). \n"
                      "This is an incorrect Polybius Cipher.")
                oops = True
                itera -= itera
            except IndexError:
                print("Error: Odd number of digits. \n"
                      "This is an incorrect Polybius Cipher.")
                oops = True
                itera -= itera
        if oops:
            return "No decryption available."
        else:
            output = ''.join(output_list)
            return output
