import json as json
import numpy as np
from util.cipher import decrypt_mono
from util.mapping import freq,alphabet
import util.mapping as map
import util.file_reader as fr
import os


class FreqMatrix:

    def __init__(self):
        self.hashed = None
        self.matrix = np.zeros((26, 26), dtype=float)
        self.indexes = alphabet

    def swap_indexes(self, char1, char2):
        lst = list(self.indexes)
        lst[self.indexes.find(char1)], lst[self.indexes.find(char2)] = lst[self.indexes.find(char2)], lst[self.indexes.find(char1)]
        self.indexes = ''.join(lst)

    def load_expected_bigram_file(self):
        temp = os.path.join(os.path.dirname(__file__), "../../", "data/", "two_gram_rel_freq.txt")
        self.hashed = json.loads(open(temp).readline())
        for k, v in self.hashed.items():
            self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = float(v)

    def swap_cols_rows(self, char1, char2):
        index1 = self.indexes.find(char1)
        index2 = self.indexes.find(char2)
        self.matrix[:, [index1, index2]] = self.matrix[:, [index2, index1]]
        self.matrix[[index1, index2], :] = self.matrix[[index2, index1], :]
        self.swap_indexes(char1, char2)

    def load_freq_from_text(self, text):
        hashed = {}
        prepared_ret = {}
        for i in range(len(text)-1):
            if text[i:i+2] in hashed:
                temp = hashed[text[i: i+2]]
                hashed.pop(text[i:i+2])
                hashed.update({text[i:i+2]: temp+1})
            else:
                hashed.update({text[i:i+2]: 1})
        for k, v in hashed.items():
            prepared_ret.update({k: float(v/len(text))})
            self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = v/len(text)
        self.hashed = prepared_ret

    def eval_difference(self, expected_matrix, key):
        diff = 0
        for char1 in map.alphabet:
            for char2 in map.alphabet:
                diff += abs(self.matrix[self.indexes.find(decrypt_mono(char1, key)), self.indexes.find(decrypt_mono(char2, key))]-expected_matrix.matrix[expected_matrix.indexes.find(char1), expected_matrix.indexes.find(char2)])
        return diff

    def plaintext_suitable(self, file):
        self.load_freq_from_text(fr.read_file(file))
        expected = FreqMatrix()
        expected.load_expected_bigram_file()
        print(self.eval_difference(expected, alphabet))


f = FreqMatrix()
e = FreqMatrix()
# e.plaintext_suitable("plaintext1.txt")
f.load_expected_bigram_file()
# f.load_freq_from_text("aaababbbababbbbb")
e.load_freq_from_text("aabbabbbababbbbb")

