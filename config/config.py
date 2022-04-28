import random
import string

default_key = 0x8809cf4f3c2b7e151628aed2a6abf7158809cf4f3c2b7e151628aed2a6abf715
random_key = lambda a: generate_key()


def generate_key():
    key_size = 32  # number of characters in the string.
    # call random.choices() string module to find the string in Uppercase + numeric data.
    ran = ''.join(random.choices(string.hexdigits + string.digits, k=key_size))
    print("Key has been generated in HEX : " + str(ran))
    # return key in integer format
    return int(hex(int(ran, 16)), 16)


color_background_darker = (52 / 255, 73 / 255, 94 / 255, 1.0)
color_background_normal = (44 / 255, 62 / 255, 70 / 255, 1.0)
