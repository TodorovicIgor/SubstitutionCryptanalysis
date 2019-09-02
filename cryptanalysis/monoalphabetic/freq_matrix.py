import json as json
import numpy as np
from util import cipher

import util.mapping as map
import os


class FreqMatrix:

    def __init__(self):
        self.hashed = None
        self.matrix = np.zeros((26, 26), dtype=float)

    def load_expected_bigram_file(self):
        temp = os.path.join(os.path.dirname(__file__), "../../", "data/", "two_gram_rel_freq.txt")
        self.hashed = json.loads(open(temp).readline())
        for k, v in self.hashed.items():
            self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = float(v)

    def swap_cols_rows(self, char1, char2):
        self.matrix[:, [map.mapping[char1], map.mapping[char2]]] = self.matrix[:, [map.mapping[char2], map.mapping[char1]]]
        self.matrix[[map.mapping[char1], map.mapping[char2]], :] = self.matrix[[map.mapping[char2], map.mapping[char1]], :]

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
                # given guessed key calculate how close distribution matrix is to expected frequency matrix
                diff += abs(
                    self.matrix[map.mapping[cipher.decrypt_mono(char1, key)], map.mapping[
                        cipher.decrypt_mono(char2, key)]]
                    -
                    expected_matrix.matrix[map.mapping[char1], map.mapping[char2]]
                )
        return diff

'''
f = FreqMatrix()
# f.load_expected_bigram_file()
f.load_freq_from_text("aaababshdbasdjabsdjabsdajkglbab")
print(f.matrix)
'''