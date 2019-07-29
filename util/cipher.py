import re
from util import mapping as map


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


def encrypt(plain, key):
    if type(key) == str:
        # poly alphabetic encryption
        # fit key size to plaintext size
        key = key * (len(plain) // len(key)+1)
        # format plaintext
        plain = transform(plain)
        crypted = ""
        for i in range(len(plain)):
            crypted += encrypt_char(plain[i], key[i])
        return crypted
    if type(key) == int:
        # mono alphabetic encryption
        # format plaintext
        plain = transform(plain)
        crypted = ""
        for i in range(len(plain)):
            crypted += encrypt_char(plain[i], key)
        return crypted


def decrypt(cipher, key):
    if type(key) == str:
        # poly alphabetic decryption
        # fit key size to plaintext size
        key = key * (len(cipher) // len(key) + 1)
        plain = ""
        for i in range(len(cipher)):
            plain += decrypt_char(cipher[i], key[i])
        return plain
    if type(key) == int:
        # mono alphabetic decryption
        plain = ""
        for i in range(len(cipher)):
            plain += decrypt_char(cipher[i], key)
        return plain


# TESTING
'''
plain = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
key = "key"
c = encrypt(plain, 1)
print(c)
print(decrypt(c, 1))
'''
