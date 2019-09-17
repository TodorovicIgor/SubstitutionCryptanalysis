import json as json
import numpy as np
from util.cipher import decrypt_mono, transform
from util.mapping import freq,alphabet
import util.mapping as map
import util.file_reader as fr
import os
import pprint


class FreqMatrix:

    def __init__(self):
        self.hashed = None
        self.matrix = np.zeros((26, 26), dtype=float)

    def load_expected_bigram_file(self):
        temp = os.path.join(os.path.dirname(__file__), "../../", "data/", "two_gram_rel_freq.txt")
        self.hashed = json.loads(open(temp).readline())
        for k, v in self.hashed.items():
            self.matrix[alphabet.find(k[0]), alphabet.find(k[1])] = float(v)

    def swap_cols_rows(self, char1, char2):
        index1 = alphabet.find(char1)
        index2 = alphabet.find(char2)
        self.matrix[:, [index1, index2]] = self.matrix[:, [index2, index1]]
        self.matrix[[index1, index2], :] = self.matrix[[index2, index1], :]
        # self.swap_indexes(char1, char2)

    def load_freq_from_text(self, text):
        # treba da se proveri
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
            # self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = v/len(text)
            self.matrix[alphabet.find(k[0]), alphabet.find(k[1])] = v/len(text)
        self.hashed = prepared_ret

    def load_freq_from_files(self, files):
        total_text_length = 0
        for f in files:
            text = f.file_reader.read_file(f)

    def eval_difference(self, expected_matrix):
        diff = 0
        for char1 in map.alphabet:
            for char2 in map.alphabet:
                # diff += abs(self.matrix[self.indexes.find(decrypt_mono(char1, key)), self.indexes.find(decrypt_mono(char2, key))]-expected_matrix.matrix[expected_matrix.indexes.find(char1), expected_matrix.indexes.find(char2)])
                diff += abs(self.matrix[alphabet.find(char1), alphabet.find(char2)]-expected_matrix.matrix[alphabet.find(char1), alphabet.find(char2)])
        return diff

    def eval_difference_test(self, expected_matrix):
        diff = 0
        for char1 in map.alphabet:
            for char2 in map.alphabet:
                # diff += abs(self.matrix[self.indexes.find(decrypt_mono(char1, key)), self.indexes.find(decrypt_mono(char2, key))]-expected_matrix.matrix[expected_matrix.indexes.find(char1), expected_matrix.indexes.find(char2)])
                print("char1 is", char1, ", char2 is", char2)
                print("distr is ", self.matrix[alphabet.find(char1), alphabet.find(char2)], "expected is ", expected_matrix.matrix[alphabet.find(char1), alphabet.find(char2)])
                print("difference is", self.matrix[alphabet.find(char1), alphabet.find(char2)]-expected_matrix.matrix[alphabet.find(char1), alphabet.find(char2)], "************************")
                diff += abs(self.matrix[alphabet.find(char1), alphabet.find(char2)]-expected_matrix.matrix[alphabet.find(char1), alphabet.find(char2)])
        print("sum is", diff)
        return diff

    def plaintext_suitable(self, file):
        self.load_freq_from_text(fr.read_file(file))
        expected = FreqMatrix()
        expected.load_expected_bigram_file()
        print(self.eval_difference(expected))

    # def print_indexes(self):
    #     print(self.indexes)
    #
    def print_matrix(self):
        for char1 in map.alphabet:
            for char2 in map.alphabet:
                print(char1, char2, self.matrix[alphabet.find(char1), alphabet.find(char2)])


# t = FreqMatrix()
# t.load_freq_from_text(transform("etaoatotoatataotteoattttaetoaotoatoeoteotatet"))
# t.print_indexes()
# t.print_matrix()
# print('*************************************************************************************************')
# t.swap_cols_rows('e', 't')
# t.print_indexes()
# t.print_matrix()

# e = FreqMatrix()
# e.load_expected_bigram_file()
# e.print_matrix()
# e.print_indexes()
