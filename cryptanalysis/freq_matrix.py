import json as json
import numpy as np
import util.mapping as map


class FreqMatrix:

    def __init__(self):
        self.hashed = None
        self.matrix = np.arange(26*26).reshape(26, 26)
        print(self.matrix)

    def load_expected_bigram_file(self):
        self.hashed = json.loads(open("../data/two_gram_rel_freq.txt").readline())
        for k, v in self.hashed.items():
            print(v)
            self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = v
        print(self.matrix)
        self.matrix[0, 0] = 5

f = FreqMatrix()
f.load_expected_bigram_file()
