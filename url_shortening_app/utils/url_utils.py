"""
Core logic located here to avoid filling our views up with extra fluff
"""
import math

unique_index = 0
b62_mapping = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
len_base = len(b62_mapping)

def url_conversion(method, url):
    if method == 'encode':
        global unique_index
        unique_index += 1
        number = unique_index
        encoded = ''

        while number > 0:
            remainder = number % len_base
            encoded = b62_mapping[int(remainder)] + encoded
            number = int(number / len_base)

        d = dict()
        d['encoded_value'] = encoded
        d['unique_index'] = unique_index

        return d

    else:
        # Code gap: Assuming decoding url will only be given in this format
        url = url.split('https://change.co/')[1]
        total = 0
        reversed_key = url[::-1]
        for i, char in enumerate(reversed_key):
            total += b62_mapping.index(char) * int(math.pow(len_base, i))

        return total
