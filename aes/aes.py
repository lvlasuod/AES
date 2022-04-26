from aes.aes_utils import *
import numpy as np


class AES:

    def __init__(self, master_key, rounds=10):
        self.master_key = master_key
        self.rounds = rounds

    def encrypt(self, s):

        s = self.convertToMatrix(s.encode("utf-8").hex())
        #s = self.add_key(s)
        # TODO  add key

        for i in range(1, self.rounds):
            self.use_s_box(s)
            # TODO  shift rows
            # TODO  mix columns
            #s = self.add_key(s)
            # TODO  add key

        self.use_s_box(s)
        # TODO shift rows
        #s = self.add_key(s)
        # TODO add key

        s = self.convertToText(s)
        return s

    def decrypt(self, s):

        s = self.convertToMatrix(s)

        # TODO  add key
        #s = self.add_key(s)
        # TODO  inv shift rows
        self.use_inv_s_box(s)

        for i in range(1, self.rounds):
            # TODO  add key
            # TODO  inv mox columns
            # TODO  inv shift rows
            self.use_inv_s_box(s)

        # TODO add key
        #s = self.add_key(s)

        s = self.convertToText(s)
        return s

    def convertToMatrix(self, text):
        """ Converts an array into a matrix.  """
        return [list(text[i:i + 4]) for i in range(0, len(text), 4)]

    def keyToMatrix(self, text):
        """ Converts an array into a matrix.  """
        return [list(text[i + 4:i]) for i in range(0, len(text), 4)]
    def convertToText(self, s):
        """ Converts an array into a matrix.  """
        text = ""
        for i in range(len(s)):
            for j in range(4):
                text += s[i][j]
        return text

    def use_s_box(self, s):
        for i in range(len(s)):
            for j in range(4):
                s[i][j] = chr(s_box[ord(s[i][j])])
        return s

    def use_inv_s_box(self, s):
        for i in range(len(s)):
            for j in range(4):
                s[i][j] = chr(inv_s_box[ord(s[i][j])])
        return s

    def add_key(self, s):
        print(self.master_key)
        arr = np.reshape(self.master_key, (4, -1))
        print(arr)
        #arr = np.asmatrix(arr)
        #print(np.asmatrix(arr))
        #s =np.asmatrix(s)
        print(s)
        o = np.dot(s,arr)
        print(o)
        return o
