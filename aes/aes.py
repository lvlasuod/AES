from aes.aes_utils import *


class AES:
    rounds_by_key_size = {16: 10, 24: 12, 32: 14}
    def __init__(self, master_key):
        #assert len(master_key) in AES.rounds_by_key_size
        #self.n_rounds = AES.rounds_by_key_size[len(master_key)]
        #self._key_matrices = self._expand_key(master_key)
        pass

    def convertToMatrix(self,text):
        return convert_to_matrix(text)

    def use_s_box(self,s):
        return sub_bytes(s)

    def use_inv_s_box(self,s):
        return inv_sub_bytes(s)