import string
import random

class Confidential:
    '''
    Confidential encrypts all your texts!

    Parameters
    ----------
    text : str
        A string containing only ASCII letters

    Examples
    --------
    >>> from confidential import Confidential
    >>> mysecret = Confidential("Which wristwatches are swiss wristwatches")
    >>> mysecret.caesar(1)
    'XIJD IXSJ TUXB UDIF TBSF TXJT TXSJ TUXB UDIF T'

    Notes
    -----
    Do not use this simple techniques to encrypt important information.

    References
    ----------
    `Classical encryption techniques
    <https://www.codeproject.com/Articles/63432/Classical-Encryption-Techniques>`_`
    '''
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("Message has to be a string.")
        if all(ord(c) < 128 for c in text):
            self.original_text = text
            self.text = text.lower()
            self.text_numbers = self._convert_text()
        else:
            raise SyntaxError("Text Contains non-ASCII characters")
    
    def frequency(self, text=None):
        '''
        Produces the letters frequency of an input text or the original if none is
        provided.
        '''
        if text is None:
            text = self.text
        return {n:text.count(n) for n in set(text) if n in string.ascii_letters}

    def _convert_text(self):
        '''
        Produce a list containing the conversion from letters to numbers for the
        text in the object such: a -> 0, b -> 1, ...
        '''
        text_in_numbers = filter(lambda x: ord('a') <= x <= ord('z'), map(ord, self.text))
        return list(map(lambda x: x - ord('a'), text_in_numbers))

    def _convert_numbers(self, numbers):
        '''
        Converts to crypto-shaped text a series of numbers such that 0 -> A, 1 -> B, ...
        A crypto-shaped text is formed of blocks of four letters separated by spaces.
        '''
        numbers_in_text = list(map(lambda x: chr(x + 65), numbers))
        return ' '.join([''.join(numbers_in_text[i:i+4]) for i in range(0, len(numbers_in_text), 4)])

    def caesar(self, k):
        '''
        Caesar cipher method. A simple substitution algorithm that shifts the letters
        a determined number (`k`) of positions.

        Parameters
        ----------
        k : int
           The shift amount for the encrypted message.
        '''
        shifted_text = map(lambda x: (x + k) % 26, self.text_numbers)
        return self._convert_numbers(shifted_text)

    def mono(self, key=None):
        if not key:
            key = self._generate()
        else:
            key = self._parse_keys(key)
        self.mono_key = key
        shuffle_text = map(key.get, self.text_numbers)
        return self._convert_numbers(shuffle_text)

    def _parse_keys(self, key):
        '''
        Is your key good enough for the encryption?
        Keys need to provide a mapping between message letters and encrypted ones.
        This will parse a characters key into a numeric one.

        Parameters
        ----------
        key : dict
            A dictionary with all the letters in the alphabet and the corresponding
            for the message.
        '''
        try:
            all_keys = ''.join(map(str, sorted(key.keys())))
        except AttributeError as e:
            raise TypeError("key needs to be a dictionary.")

        if all_keys == ''.join([chr(x+97) for x in range(26)]):
            key = {ord(x) - ord('a'): ord(y) - ord('A') for x, y in key.items()}

        if sorted(key.keys()) != list(range(26)):
            raise ValueError("Some letters are missing as keys.")
        if sorted(key.values()) != list(range(26)):
            raise ValueError("Some letters are missing as values.")
        return key

    def _generate(self):
        letters = list(range(26))
        random.shuffle(letters)
        return {x: y for x, y in zip(range(26), letters)} #whatever the letters are
   