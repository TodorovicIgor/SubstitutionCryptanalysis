from cryptanalysis.monoalphabetic import freq_matrix, key
from util import cipher, mapping, file_reader
import copy


class Analyzer:

    def __init__(self, ciphertext):
        self.expected = freq_matrix.FreqMatrix()
        self.expected.load_expected_bigram_file()
        self.distribution = freq_matrix.FreqMatrix()
        self.key = key.Key(mapping.freq)  # step 1
        self.plaintext = None
        self.ciphertext = ciphertext
        self.current_difference = float('inf')
        self.best_difference = float('inf')
        self.distribution.load_freq_from_text(cipher.decrypt_mono(self.ciphertext, self.key.get_key()))  # step 2
        # self.distribution.load_freq_from_text(self.ciphertext)  # step 2

    def break_cipher(self):
        print("Cipher is", self.ciphertext)
        self.best_difference = self.distribution.eval_difference(self.expected, self.key.get_key())  # step 3
        # a = b = 0  # step 0
        print("Starting function value is ", self.best_difference, "key is", self.key.key)
        new_iteration = True
        while new_iteration:
            new_iteration = False
            print("started new iteration\n\n\n\n")
            for char1 in mapping.freq:
                for char2 in mapping.freq:
                    print("\nCurrent key is \t", self.key.get_key())
                    new_key = copy.copy(self.key)  # step 4
                    new_distribution = copy.copy(self.distribution)  # step 5

                    new_key.swap(mapping.freq.find(char1), mapping.freq.find(char2))    # step 6a

                    print("New key is \t\t", new_key.get_key(), "swapped", char1, "and", char2)
                    new_distribution.swap_cols_rows(char1, char2)  # step 7
                    current_difference = new_distribution.eval_difference(self.expected, new_key.get_key())  # step 8
                    print("New function value is", current_difference, "with net", self.best_difference-current_difference)
                    if current_difference < self.best_difference:  # step 9
                        # a = b = 0  # step 9a
                        new_iteration = True
                        print("Found better key:", new_key.get_key(), ", better function value is", current_difference, "************************************")
                        self.best_difference = copy.copy(current_difference)    # step 10
                        self.key = copy.copy(new_key)                           # step 11
                        self.distribution = copy.copy(new_distribution)         # step 12
        # step 13

        print(self.distribution.matrix)

        print("Best key is:", self.key.get_key())
        print("Best difference is", self.best_difference)
        print("text is", cipher.decrypt_mono(self.ciphertext, self.key.get_key()))


# plaintext2 = file_reader.read_file("plaintext2.txt")
# ciphertext2 = cipher.encrypt_mono(plaintext2, "abcdefghijklmnopqrstuvwxyz")
# # a = Analyzer(cipher.transform(plaintext))
# a = Analyzer(ciphertext2)
# a.break_cipher()
