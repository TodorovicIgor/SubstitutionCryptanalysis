import re
from util import mapping as map
# import cryptanalysis.monoalphabetic.freq_matrix as freq_matrix


def transform(string, regex=r"[a-z]"):
    s = string.lower()
    ret = ""
    for c in s:
        if re.match(regex, c):
            ret += c
    return ret


def encrypt_char(p, k):
    if type(k) == str:
        c = (map.mapping[p] + map.mapping[k]) % 26
        return map.mapping[c]
    if type(k) == int:
        c = (map.mapping[p] + k) % 26
        return map.mapping[c]


def decrypt_char(c, k):
    if type(k) == str:
        p = (map.mapping[c] - map.mapping[k]) % 26
        return map.mapping[p]
    if type(k) == int:
        p = (map.mapping[c] - k) % 26
        return map.mapping[p]


def encrypt_poly(plain, key):
    # fit key size to plaintext size
    key = key * (len(plain) // len(key)+1)
    # format plaintext
    plain = transform(plain)
    cipher = ""
    for i in range(len(plain)):
        cipher += encrypt_char(plain[i], key[i])
    return cipher


def decrypt_poly(cipher, key):
    # fit key size to plaintext size
    key = key * (len(cipher) // len(key) + 1)
    plain = ""
    for i in range(len(cipher)):
        plain += decrypt_char(cipher[i], key[i])
    return plain


def generate_key_mono(key):
    ret = key
    for char in map.alphabet:
        if char not in key:
            ret += char
    return ret


# def analize_plaintext(plaintext):
#     plaintext = transform(plaintext)
#     expected = freq_matrix.FreqMatrix()
#     expected.load_expected_bigram_file()
#     distribution = freq_matrix.FreqMatrix()


def encrypt_mono(plain, key):
    key = generate_key_mono(key)
    plain = transform(plain)
    cipher = ""
    for i in range(len(plain)):
        # char from plain[i] maps to integer which is indexing substitution char in key
        cipher += key[map.mapping[plain[i]]]
    return cipher


def decrypt_mono(cipher, key):
    #print(key)
    key = generate_key_mono(key)
    plain = ""
    for i in range(len(cipher)):
        # char from cipher[i] is used to get position of plaintext char from key
        plain += map.alphabet[key.find(cipher[i])]
    return plain

# TESTING
'''
plain = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
key = "key"
c = encrypt(plain, 1)
print(c)
print(decrypt(c, 1))
'''
