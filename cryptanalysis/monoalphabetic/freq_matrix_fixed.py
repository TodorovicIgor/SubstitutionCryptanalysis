from util.mapping import alphabet
from util import cipher
import os, json


class Matrix:

    def __init__(self):
        self.expected = [[0.0 for _ in range(4)] for _ in range(4)] # 26
        self.distribution = [[0.0 for _ in range(4)] for _ in range(4)] #  26
        self.indexes = alphabet

    def load_bigram_(self):
        # temp = os.path.join(os.path.dirname(__file__), "../../", "data/", "two_gram_rel_freq.txt")
        temp = os.path.join(os.path.dirname(__file__), "../../", "data/", "test.txt")
        hashed = json.loads(open(temp).readline())
        for k, v in hashed.items():
            self.expected[self.indexes.find(k[0])][self.indexes.find(k[1])] = float(v)
        # TEST

    def swap_indexes(self, char1, char2):
        lst = list(self.indexes)
        lst[self.indexes.find(char1)], lst[self.indexes.find(char2)] = lst[self.indexes.find(char2)], lst[self.indexes.find(char1)]
        self.indexes = ''.join(lst)

    def swap_distribution(self, char1, char2):
        index1 = self.indexes.find(char1)
        index2 = self.indexes.find(char2)
        print("indeksi su: ", index1, index2)
        for i in range(4):
            temp = self.distribution[i][index1]
            self.distribution[i][index1] = self.distribution[i][index2]
            self.distribution[i][index2] = temp
        temp = self.distribution[index1]
        self.distribution[index1] = self.distribution[index2]
        self.distribution[index2] = temp

    def swap(self, char1, char2):
        self.swap_distribution(char1, char2)
        self.swap_indexes(char1, char2)

    def eval_difference(self):
        diff = 0
        for i in range(26):
            for j in range(26):
                diff += abs(self.expected[i][j] - self.distribution[i][j])
        return diff

    def suitable(self, plaintext):
        plaintext = cipher.transform(plaintext)
        # TODO
        for i in range(26):
            for j in range(26):
                pass


    def print_distribution(self):
        for i in range(4):
            print(self.distribution[i])

    def print_expected(self):
        for i in range(4):
            print(self.expected[i])

# TODO swap ne radi dobro, ne menjaju se
a = Matrix()
a.load_bigram_()
a.print_expected()
print("*********************************")
a.swap('a', 'b')
a.print_expected()
print()
