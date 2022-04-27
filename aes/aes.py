from aes.aes_utils import *
import numpy as np

xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)
A = np.array([[2, 3, 1, 1], [1, 2, 2, 3], [1, 1, 2, 3], [3, 1, 1, 2]])
B = np.array([[14, 11, 13, 9], [9, 14, 11, 13], [13, 9, 14, 11], [11, 13, 9, 14]])


class AES:
    rounds_by_key_size = {16: 10, 24: 12, 32: 14}

    def __init__(self, master_key, rounds=10):
        # assert len(master_key) in AES.rounds_by_key_size
        self.master_key = master_key
        self.rounds = rounds
        # self._key_matrices = self._expand_key(master_key)

    def encrypt(self, s):
        s = self.convertToMatrix2(s)
        print(s)
        m = self.convertToMatrix2(self.master_key)
        # print(m)
        # TODO  add key

        for i in range(1, self.rounds):
            print(f"Stage: {i}")
            s = self.use_s_box(s)
            print(f"after s_box: {s}")
            # TODO  shift rows
            s = self.shift_left(s)
            print(f"shifted: {s}")
            # TODO  mix columns
            s = self.m_column(s)
            print(s)
            # TODO  add key

        s = self.use_s_box(s)
        # TODO shift rows
        s = self.shift_left(s)
        # TODO add key

        s = self.convertToText2(s)
        return s

    def decrypt(self, s):

        s = self.convertToMatrix2(s)

        # TODO  add key
        # TODO  inv shift rows
        s = self.shift_right(s)
        s = self.use_inv_s_box(s)

        for i in range(1, self.rounds):
            # TODO  add key
            # TODO  inv mox columns
            # s = self.inv_mix_column(s)
            s = self.inv_m_column(s)
            # TODO  inv shift rows
            s = self.shift_right(s)
            s = self.use_inv_s_box(s)

        # TODO add key

        s = self.convertToText2(s)
        return s

    def convertToMatrix(self, text):
        """ Converts an array into a matrix.  """
        return [list(text[i:i + 4]) for i in range(0, len(text), 4)]

    def convertToMatrix2(self, text):
        arr_1d = np.array(list(text))
        # arr_1d = np.array(text)
        arr = np.reshape(arr_1d, (int(len(text) / 4), 4), order='F')
        return arr

    def convertToText(self, s):
        """ Converts an array into a matrix.  """
        text = ""
        for i in range(len(s)):
            for j in range(4):
                text += s[i][j]
        return text

    def convertToText2(self, s):
        """ Converts an array into a matrix.  """
        text = ""
        arr = np.ravel(s, order='F')
        for i in range(len(arr)):
            text += arr[i]
            # np.ravel(s, order='F')
            # text += s[i][j]
        return text

    def use_s_box(self, s):
        for i in range(len(s)):
            for j in range(4):
                # print(int(s_box[ord(f"{s[i,j]}")]))
                # print(ord("R"))
                s[i, j] = chr(s_box[ord(s[i, j])])
                # print(f"{s[i, j]} ord: {s_box[s[i, j]]}")
        return s

    def use_inv_s_box(self, s):
        for i in range(len(s)):
            for j in range(4):
                s[i, j] = chr(inv_s_box[ord(s[i, j])])
        return s

    def shift_right(self, s):
        new_rows = []
        i = 0
        for row in s:
            if i > 0:
                for j in range(i):
                    # row = row[-1:] + row[:len(row) - 1]
                    row = np.roll(row, i)

            new_rows.append(row)
            i += 1
        s = new_rows
        return np.array(s)

    def shift_left(self, s):
        new_rows = []
        i = 0

        for row in s:
            if i > 0:
                for j in range(i):
                    # row = row[1:] + row[:1]
                    row = np.roll(row, i * -1)

            new_rows.append(row)
            i += 1
        s = np.array(new_rows)
        return s

    def mix_column(self, s):
        new_rows = []
        for row in s[1:]:
            new_rows.append(row)
        new_rows.append(s[0])
        return new_rows

    def inv_mix_column(self, s):
        new_rows = []
        new_rows.append(s[-1])
        for row in s[:-1]:
            new_rows.append(row)
        return new_rows

    def to_Ascii(self, s):
        new_rows = []
        ascii = ' '.join(str(ord(c)) for c in s)
        new_rows = np.fromstring(ascii, dtype=int, sep=' ')
        print(new_rows)

        return new_rows

    def Array_To_Ascii(self, s):
        new_s = []
        for row in s:
            temp = self.to_Ascii(row)
            new_s.append(temp)
            print(new_s)

        return np.transpose(new_s)

    def Array_To_Letters(self, s):
        new_a = []
        for row in s:
                new_s = np.array(list(''.join(str(chr(c)) for c in row)))
                new_a.append(new_s)

        print(new_a)
        return new_a

    xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    def mix_single_column(self, a):
        # see Sec 4.1.2 in The Design of Rijndael
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ xtime(a[0] ^ a[1])
        a[1] ^= t ^ xtime(a[1] ^ a[2])
        a[2] ^= t ^ xtime(a[2] ^ a[3])
        a[3] ^= t ^ xtime(a[3] ^ u)
        return a

    def mix_columns(self, s):
        new_s = []
        s = np.transpose(s)
        for i in range(len(s)):
            temp = self.mix_single_column(s[i])
            new_s.append(temp)
            print(new_s)

        return np.transpose(new_s)

    def inv_mix_columns(self,s):
        new_s = []
        # see Sec 4.1.3 in The Design of Rijndael
        s2 = np.transpose(s)
        for i in range(len(s2)):
            u = xtime(xtime(s2[i][0] ^ s2[i][2]))
            v = xtime(xtime(s2[i][1] ^ s2[i][3]))
            s2[i][0] ^= u
            s2[i][1] ^= v
            s2[i][2] ^= u
            s2[i][3] ^= v
        s2 = np.transpose(s2)
        new_s = self.mix_columns(s2)
        return new_s

    def m_column(self, s):
        temp = self.Array_To_Ascii(s)
        print(f"ascii: {temp}")
        #mix = np.dot(A, temp)

        mixcol = self.mix_columns(temp)
        print("mixcol")
        print(mixcol)
        #remixcol = self.inv_mix_columns(mixcol)

        #print("remixcol")
        #print(remixcol)
        final = self.Array_To_Letters(np.transpose(mixcol))
        print(final)
        return np.array(final)

    def inv_m_column(self, s):
        temp = self.Array_To_Ascii(s)
        print(f"ascii: {temp}")

        remixcol = self.inv_mix_columns(temp)

        print("remixcol")
        print(remixcol)
        final = self.Array_To_Letters(np.transpose(remixcol))
        print(final)
        return np.array(final)

    def add_key(self, s):
        print(self.master_key)
        arr = np.reshape(self.master_key, (4, -1))
        print(arr)
        # arr = np.asmatrix(arr)
        # print(np.asmatrix(arr))
        # s =np.asmatrix(s)
        print(s)
        o = np.dot(s, arr)
        print(o)
        return o
