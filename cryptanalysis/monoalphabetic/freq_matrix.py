import json as json
import numpy as np
import util.mapping as map


class FreqMatrix:

    def __init__(self):
        self.hashed = None
        #self.matrix = np.arange(5*5).reshape(5, 5)
        self.matrix = np.empty((26, 26,))

    def load_expected_bigram_file(self):
        self.hashed = json.loads(open("../data/two_gram_rel_freq.txt").readline())
        for k, v in self.hashed.items():
            self.matrix[map.mapping[k[0]], map.mapping[k[1]]] = float(v)
        print(self.matrix)

    def swap_cols_rows(self, row1, row2, col1, col2):
        print(self.matrix)
        self.matrix[:, [col1, col2]] = self.matrix[:, [col2, col1]]
        self.matrix[[row1, row2], :] = self.matrix[[row2, row1], :]
        print(self.matrix)
