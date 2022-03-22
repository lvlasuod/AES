from aes.aes_utils import *


class AES:
    rounds_by_key_size = {16: 10, 24: 12, 32: 14}
    def __init__(self, master_key, rounds=10):
        #assert len(master_key) in AES.rounds_by_key_size
        self.rounds = rounds
        #self._key_matrices = self._expand_key(master_key)


    def encrypt(self,s):

        s = self.convertToMatrix(s)

        # TODO  add key

        for i in range (1,self.rounds):
            self.use_s_box(s)
            # TODO  shift rows
            # TODO  mix columns
            # TODO  add key

        self.use_s_box(s)
        # TODO shift rows
        # TODO add key

        # TODO  return matrix converted to string ( inverse of self.convertToMatrix(s))
        pass

    def decrypt(self,s):

        s = self.convertToMatrix(s)

        # TODO  add key
        # TODO  inv shift rows
        self.use_inv_s_box(s)

        for i in range (1,self.rounds):
            # TODO  add key
            # TODO  inv mox columns
            # TODO  inv shift rows
            self.use_inv_s_box(s)

        # TODO add key

        # TODO  return matrix converted to string ( inverse of self.convertToMatrix(s))
        pass

    def convertToMatrix(self,text):
        return convert_to_matrix(text)

    def use_s_box(self,s):
        return sub_bytes(s)

    def use_inv_s_box(self,s):
        return inv_sub_bytes(s)
